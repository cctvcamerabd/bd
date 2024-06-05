import os
import subprocess

def download_website(url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    command = [
        "wget",
        "--mirror",
        "--convert-links",
        "--adjust-extension",
        "--page-requisites",
        "--no-parent",
        "--directory-prefix", output_folder,
        url
    ]
    
    subprocess.run(command)

if __name__ == "__main__":
    url = "https://www.startech.com.bd/"
    output_folder = "offline_website"

    download_website(url, output_folder)
    print(f"Website downloaded successfully and saved in '{output_folder}' folder.")
