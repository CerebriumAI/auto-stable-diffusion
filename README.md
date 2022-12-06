# auto-stable-diffusion

1. Create a new instance on Lambda labs
2. SSH into that machine
3. Create an ssh keypair `ssh-keygen -t rsa -b 4096` for GitHub access on the machine.
4. `cat ~/.ssh/id_rsa.pub` and add to https://github.com/settings/ssh/new
5. `git clone git@github.com:CerebriumAI/auto-stable-diffusion.git`
6. `cd auto-stable-diffusion`
7. `sudo chmod +x setup.sh`
8. `./setup.sh`
9. Upload images to Supabase
10. `./run-all.sh`
11. Wait while it trains the model, creates a few images and uploads the results to supabase
12. If you want to push to HF, set some ENV vars and run `python push_to_hub.py`
