echo "Download input images from Supabase"
python download-images.py

echo "Run training for each uuid folder"
for UUID_folder in images/unprocessed/*/ ; do

    a=($(echo "$UUID_folder" | tr '/' '\n'))
    UUID=${a[2]}

    export HF_TOKEN=$(cat ~/.huggingface/token)
    export MODEL_NAME="runwayml/stable-diffusion-v1-5"
    export INSTANCE_DIR="images/unprocessed/${UUID}"
    export OUTPUT_DIR="./weights/${UUID}"
    export CLASS_DIR="./class-images"
    export CLASS_TYPE="person"

    FILE_COUNT=$(find "$UUID_folder" | wc -l)

    export NUM_TRAIN_STEPS=$((FILE_COUNT * 100))

    echo "Number of images: $FILE_COUNT"

    if ((FILE_COUNT < 5)); then
      break
    fi

    accelerate launch ./diffusers/examples/dreambooth/train_dreambooth.py \
      --class_data_dir="$CLASS_DIR" \
      --class_prompt="a photo of a ${CLASS_TYPE}" \
      --gradient_accumulation_steps=1 \
      --instance_data_dir="$INSTANCE_DIR" \
      --instance_prompt="a photo of ${UUID} ${CLASS_TYPE}" \
      --learning_rate=1e-6 \
      --lr_scheduler="constant" \
      --lr_warmup_steps=0 \
      --max_train_steps=$NUM_TRAIN_STEPS \
      --mixed_precision="fp16" \
      --num_class_images=100 \
      --output_dir="$OUTPUT_DIR" \
      --pretrained_model_name_or_path=$MODEL_NAME  \
      --prior_loss_weight=1.0 \
      --resolution=512 \
      --revision="fp16" \
      --sample_batch_size=4 \
      --seed=1337 \
      --train_batch_size=1 \
      --train_text_encoder \
      --with_prior_preservation

  echo "Move unprocessed images to processed folder"
  mv images/unprocessed/"$UUID" images/processed/"$UUID"

  echo "Push model to file to Huggingface"
  python push_to_hub.py "$UUID" "$OUTPUT_DIR" "$HF_TOKEN"

  echo "Run inference"
  python infer.py "$UUID" "$CLASS_TYPE" "$NUM_TRAIN_STEPS"

  echo "Upload output images to Supabase"
  python upload-images.py

done
