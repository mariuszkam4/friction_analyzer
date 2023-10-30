echo "Enter the path to the folder you want to share with the container:"
read user_path

if [ ! -d "$user_path" ]; then
	echo "The indicated folder does not exist. Try again."
	exit 1

fi

docker run -it -v "${user_path}:/shared_directory" friction_analyzer:latest

