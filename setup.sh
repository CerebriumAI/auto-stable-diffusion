echo "1. Clone repo and install diffusers"
git clone git@github.com:ShivamShrirao/diffusers.git
pip install -qq git+https://github.com/ShivamShrirao/diffusers@cecdd8bdd1c0ac902483e464f40ebdaa91f3fe13
pip install -U -r diffusers/examples/dreambooth/requirements.txt

echo "2. Install supabase packages"
pip install storage3 supabase

echo "3. Login to hugging face"
mkdir -p ~/.huggingface
export HUGGINGFACE_TOKEN="<HF_TOKEN>"
echo -n "$HUGGINGFACE_TOKEN" > ~/.huggingface/token

echo "4. Create image directories"
mkdir images images/processed images/unprocessed images/output

echo "Setup finished."