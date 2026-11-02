from pathlib import Path

def main():
    directory = Path.cwd()
    old_text = "roblox.com"
    new_text = "rowine.lol"

    for file_path in directory.glob("*.xml"):
        try:
            content = file_path.read_text(encoding="utf-8")
            updated_content = content.replace(old_text, new_text)

            if updated_content != content:
                file_path.write_text(updated_content, encoding="utf-8")
                print(f"Modified: {file_path.name}")
            else:
                print(f"No changes needed: {file_path.name}")

        except (OSError, UnicodeDecodeError) as error:
            print(f"Error processing {file_path.name}: {error}")

    print("Finished processing XML files.")

if __name__ == "__main__":
    main()