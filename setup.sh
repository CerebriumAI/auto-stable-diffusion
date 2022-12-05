echo "1. Clone repo and install diffusers"
git clone git@github.com:ShivamShrirao/diffusers.git
pip install git+https://github.com/ShivamShrirao/diffusers.git
pip install -U -r diffusers/examples/dreambooth/requirements.txt

echo "2. Install supabase packages"
pip install storage3 supabase

echo "3. Login to hugging face"
mkdir -p ~/.huggingface
echo -n "<YOUR_HF_TOKEN>" > ~/.huggingface/token

echo "4. Create image directories"
mkdir images images/processed images/unprocessed images/output

echo "Setup finished."