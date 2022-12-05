echo "1. Clone repo"
git clone git@github.com:ShivamShrirao/diffusers.git
pip install git+https://github.com/ShivamShrirao/diffusers.git
pip install -U -r diffusers/examples/dreambooth/requirements.txt
pip install storage3 supabase

echo "2. Login to hugging face"
mkdir -p ~/.huggingface
echo -n "<YOUR_HF_TOKEN>" > ~/.huggingface/token

echo "3. Done."