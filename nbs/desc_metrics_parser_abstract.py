import abc

class ParserAbstract(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_class_nodes(self, root_node):
        pass
    
    @abc.abstractmethod
    def find_method_names(self, class_node, file_bytes):
        pass
    
    @abc.abstractmethod
    def find_field_names(self, class_node, method_names, file_bytes):
        pass
    
    @classmethod
    def find_identifier_occurences(cls, node, identifier, file_bytes):
        """Counts the number of leaf nodes in an AST with a specified identifier"""
        if len(node.children) > 0:
            count = 0
            for i in node.children:
                count += ParserAbstract.find_identifier_occurences(i, identifier, file_bytes)
            return count
        else:
            word = ""
            for i in range(node.start_byte, node.end_byte):
                num_index_fails = 0
                try:
                    word += chr(file_bytes[i])
                except IndexError:
                    num_index_fails += 1
            if(num_index_fails):
                print(f"INDEX ERROR in 'find_identifier_occurences' ({num_index_fails} times)")
                print("Start byte:", node.start_byte, "End byte:", node.end_byte, "Word:", word)
            if word == identifier:
                return 1
            else:
                return 0

    @abc.abstractmethod
    def distinct_field_calls(self, class_node, field_names, file_bytes):
        pass