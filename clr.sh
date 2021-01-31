sudo cat log.txt >> history.txt
sudo echo "-------------- END OF SESSION --------------" >> history.txt
sudo echo "     " `date` >> history.txt
sudo echo "--------------------------------------------" >> history.txt
sudo echo "" >> history.txt
sudo rm -r log.txt
sudo touch log.txt
sudo chmod 777 log.txt
