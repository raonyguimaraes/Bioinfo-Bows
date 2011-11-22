#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Raony Guimarães
# Email: raonyguimaraes@gmail.com
# URL: http://

#import the goods!
import sys
import os

#include database connection
execfile('database.py')


#Description: Run Blast

class RunBlast:
    
  #def __init__(self):
    #print "Init"

  def main(self):
    print "Main"
    
    self.get_newjobs('triptofano');
    
    #select from database
    #run blast with data
    #command = 'blastall -i <query> -d /home/cenabid/db/uniprot_11_2011 -p blastp -o saida -F F -a 4 -m'
    #os.system("ls -l")
    #os.system(command)
    
  def get_newjobs(self, application_code):
    sql = "SELECT * FROM PROCESS WHERE application_code = '%s' and status = 1" % (application_code)
    cursor.execute(sql)
    
    
  def change_status(self, process_id, status_id):
    sql = "UPDATE process SET status=%s WHERE id=%s;" % (status_id, process_id)
    
  def check_status(self, process_id):
    sql = "SELECT * from process_param WHERE process_id=%s" % (process_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
      snps[x['name'].lower()] = x['id']
    
    return snps
  
  def get_process(self):
    sql = "SELECT text_value FROM process_param WHERE process_id = 150 AND name = 'fasta';"
    
    sql = "SELECT * FROM process WHERE application_code = '%s';" % ('triptofano')
    
 
  
      




if __name__ == "__main__":
    client = RunBlast()
    client.main()

