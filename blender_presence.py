from pypresence import Presence
import time

# run this in a virtual environment (source env/venv-blender/bin/activate)
# Replace this with your actual Client ID from the Developer Portal
client_id = ""
RPC = Presence(client_id)

try:
    print("Trying to connect to Discord")
    RPC.connect()
    print("Connected")

    # Set the Rich Presence
    RPC.update(
        details="Working in Blender",
        state="Blender nyeheyheh",
        large_image="blender_logo",  # This should match the image key in your Discord application
        large_text="Blender",
        start=time.time()
        )
    print("Presence set, check your Discord profile")
    
    # Keep it running for 1 minutes so Discord can show it
    while True:
        time.sleep(1)

except Exception as e:
    print(f"Something went wrong: {e}")
finally:
    try:
        RPC.clear()
        RPC.close()
        print("Presence cleared")
    except:
        pass
