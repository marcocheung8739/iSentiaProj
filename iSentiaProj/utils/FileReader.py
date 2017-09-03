'''
This class provides all required basic python functionalities  
'''
class FileReader(object):
    def read_file(self, filePath):
        try:
            fileReader = open(filePath, 'r')
            prop = {}
            for line in fileReader:
                if line.find('=') > 0:
                    line = line.strip()
                    index = line.index('=')
                    properties_key = line[0:index]
                    properties_value = line[index+1:]
                    prop[properties_key] = properties_value
        except Exception, e:
            raise e
        else:
            fileReader.close()

        return prop
        
        