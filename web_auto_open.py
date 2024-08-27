import subprocess

def open_links_in_incognito_chrome(file_path):
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
            for link in links:
                link = link.strip()
                # Use subprocess to call Chrome with incognito flag
                subprocess.Popen(['start', 'chrome', '--incognito', link], shell=True)
        print("Links opened successfully in Chrome (incognito mode)!")
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    file_path = "file_link_my.txt"  # Update this with your file path
    open_links_in_incognito_chrome(file_path)
