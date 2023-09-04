# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    # Naive solution:
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

def process_queries_faster(queries):
    # Faster solution: To be honest, this solution is kind of cheating.
    # It just uses a big fat ass array with numbers as keys to store
    # information. There is really nothing smart happening here.
    l = [None] * 10000000
    result = []
    for cur_query in queries:
        if cur_query.type == 'add':
            l[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            l[cur_query.number] = None
        else:
            if l[cur_query.number] == None:
                response = 'not found'
            else:
                response = l[cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries_faster(read_queries()))

