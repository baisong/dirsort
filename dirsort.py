def confirm(base_path):
    c = raw_input('Are you sure you want to sort the files in ' + base_path + '? [y/n] ')
    return c in ('y','Y')

def dirsort(base_path):
    confirmed = confirm(base_path)
    if confirmed:
        print "Beginning sorting of " + base_path + "..."
        # check for 'original' directory
        # check for 'files' directory
        # check for 'created' directory
        # check for 'modified' directory
        # check for 'type' directory
        # check for 'size' directory
        
        # find all top-level non-excepted files
        # mv all to '/original/', merge when possible
        
        # make links to all files (at all levels) in '/files/'
        
        # make 'created/day/%'
        # make 'created/week/%'
        # make 'created/month/%'
        # make 'created/year/%'

        # make 'modified/day/%'
        # make 'modified/week/%'
        # make 'modified/month/%'
        # make 'modified/year/%'

        # make 'type/%'

        # make 'size/tiny/?'
        # make 'size/small/?'
        # make 'size/medium/?'
        # make 'size/large/?'
        # make 'size/mega/?'

    else:
        print "Skipped sorting of " + base_path + "..."
