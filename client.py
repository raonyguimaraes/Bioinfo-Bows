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
   
  def get_newjobs(self, application_code):
    sql = "SELECT * FROM process WHERE application_code = '%s' and status = 1" % (application_code) # status 1 = NEW
    cursor.execute(sql)
    jobs = cursor.fetchall()
    
    return jobs
  def change_status(self, process_id, status_id):
    sql = "UPDATE process SET status=%s WHERE id=%s;" % (status_id, process_id)
    cursor.execute(sql)
    
  def check_status(self, process_id):
    sql = "SELECT * FROM process_param WHERE process_id=%s" % (process_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
      snps[x['name'].lower()] = x['id']
    
    return snps
  
  def get_process(self):
    sql = "SELECT text_value FROM process_param WHERE process_id = 150 AND name = 'fasta';"
    
    sql = "SELECT * FROM process WHERE application_code = '%s';" % ('triptofano')
    
  def process(self, job):
    #change status to running!
    print "Changing status from job"
    self.change_status(job['id'], 2)
    #command = 'blastall -i <query> -d /home/cenabid/db/uniprot_11_2011 -p blastp -o saida -F F -a 4 -m'
    #os.system("ls -l")
    #os.system(command)
  
  def main(self):
    print "Main"
    
    jobs = self.get_newjobs('triptofano');
    #Change state to running (2)
    for job in jobs:
      print "Processing Job: %s " % (job['id'])
      self.process(job)
    
    #select from database
    #run blast with data
    
    
    
      




if __name__ == "__main__":
    client = RunBlast()
    client.main()

