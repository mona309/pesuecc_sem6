from supabase import create_client, Client

SUPABASE_URL = "https://pamwazeccnfpxiofjsix.supabase.co/" # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBhbXdhemVjY25mcHhpb2Zqc2l4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2ODI5Mzg0OSwiZXhwIjoyMDgzODY5ODQ5fQ.lvnX6gR2DkOdtPdb9gz9sKcrHCVHvT5BtFxzkL0IGkE" # Replace with your Supabase API key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

bucket_name = "image1" # Name of the bucket to be created
image_path = r"C:\Users\Monisha\Desktop\PES2UG23CS906.jpg"  # Replace with the local image path
image_name = "PES2UG23CS906.png"  # Desired name for the uploaded file

# Step 1: Create a storage bucket
'''try:
    response = supabase.storage.create_bucket(bucket_name,   
    options={
        "public": True, # Make the bucket public
        "allowed_mime_types": ["image/png"], # Allow only PNG images
        "file_size_limit": 1024*1024, # Limit file size to 1MB
    }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Bucket creation error: {e}")'''

# # Step 2: Upload an image to the bucket
try:
    with open(image_path, 'rb') as f:
        response = supabase.storage.from_(bucket_name).upload(
            file=f, # File object
            path=image_name,  # Name of the file in the bucket
            file_options={"content-type":"image/png","cache-control": "3600", "upsert": "False"}, 
        )
        print(f"Image uploaded successfully: {response}")
except Exception as e:
    print(f"Image upload error: {e}")

# # Step 3: Get the public URL of the image

try:
    public_url =  supabase.storage.from_(bucket_name).get_public_url(
  image_name
)
    print(f"Public URL of the image: {public_url}")
except Exception as e:
    print(f"Error getting public URL: {e}")

