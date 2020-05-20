from desc_metrics_parser_abstract import ParserAbstract

class ParserJava(ParserAbstract):
    def __init__(self):
        """Define the class specific patterns to look for in a tree-sitter AST"""
        self.class_key = "class_declaration"
        self.method_key = "method_declaration"
        self.field_dec_key = "field_declaration"
        self.name_key = "identifier"

    def find_class_nodes(self, root_node):
        """Recursively searches an AST for class nodes"""
        node_list = []
        def rec_class_search(node):
            if node.type == self.class_key:
                node_list.append(node)
            for child in node.children:
                rec_class_search(child)

        rec_class_search(root_node)
        return node_list

    def find_method_names(self, class_node, file_bytes):
        """Recursively searches an AST for the identifiers of method nodes"""
        method_list = []
        def rec_method_search(node):
            if node.type == self.method_key:
                for i in node.children:
                    if i.type == self.name_key:
                        method_name = ""
                        for j in range(i.start_byte, i.end_byte):
                            method_name += chr(file_bytes[j])
                        method_list.append(method_name)
            if node.type != self.class_key:
                for child in node.children:
                    rec_method_search(child)

        for node in class_node.children:
            rec_method_search(node)
        return method_list

    def find_field_names(self, class_node, method_names, file_bytes):
        """Recursively searches an AST for the identifiers of fields/attributes"""
        class_fields = []

        def rec_name_search(node):
            if node.type == self.name_key:
                field_name = ""
                for i in range(node.start_byte, node.end_byte):
                    field_name += chr(file_bytes[i])
                class_fields.append(field_name)
            else:
                for child in node.children:
                    rec_name_search(child)

        def rec_field_search(node):
            if node.type == self.field_dec_key:
                rec_name_search(node)
            if node.type != self.class_key:
                for child in node.children:
                    rec_field_search(child)

        for node in class_node.children:
            rec_field_search(node)
        return class_fields

    def distinct_field_calls(self, class_node, field_names, file_bytes):
        """Finds the sum of the distinct field calls for each method of a class"""
        total_distinct_calls = []
     
        def rec_method_search(node):
            if node.type == self.method_key:
                distinct_method_field_calls = 0
                for field in field_names:
                    if ParserAbstract.find_identifier_occurences(node, field, file_bytes):
                        distinct_method_field_calls += 1
                total_distinct_calls.append(distinct_method_field_calls)
            if node.type != self.class_key:
                for child in node.children:
                    rec_method_search(child)

        for node in class_node.children:
            rec_method_search(node)
        return sum(total_distinct_calls)
