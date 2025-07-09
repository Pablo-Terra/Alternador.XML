import os
import xml.etree.ElementTree as ET

# Achar o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Directory found ",script_dir)
# Iterar sobre todos os arquivos XML no diretório do script
for filename in os.listdir(script_dir):
    if filename.endswith('.xml'):
        file_path = os.path.join(script_dir, filename)
        modified = False
        
        try:
            # Parse o arquivo XML f
            print( file_path,
                ''' Reading file . . .''')
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Encontrar todas as tags CPOF e modificar o texto se necessário
            for cpof_tag in root.findall('.//CFOP'):
                print("CFOP Founded")
                cpof_text = cpof_tag.text
                if cpof_text and cpof_text.strip() and cpof_text.strip()[0] == '5':
                    cpof_tag.text = '6' + cpof_text[1:]
                    modified = True
            
            # salvar o arquivo modificado se houver alterações
            if modified:
                new_filename = os.path.splitext(filename)[0] + 'MOD.xml'
                new_file_path = os.path.join(script_dir, new_filename)
                tree.write(new_file_path)
                print(f"Modified file saved as: {new_filename}")
            else:
                print(f"No modifications needed for: {filename}")
                
        except ET.ParseError:
            print(f"Error parsing XML file: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
          
