def remove_unused_references(aux_path, bib_path, out_path):
    with open(aux_path, 'r') as f:
        aux_contents = f.read()

    used_citations = set()
    for line in aux_contents.split('\n'):
        if line.startswith("\\citation{"):
            used_citations.update(line[len("\\citation{"):-1].split(','))

    with open(bib_path, 'r') as f:
        bib_contents = f.read()

    new_bib_contents = ''
    record = None
    for line in bib_contents.split('\n'):
        if line.startswith("@"):
            if record is not None and citation_key in used_citations:
                new_bib_contents += record
            record = line + '\n'
            citation_key = line.split('{', 1)[1].split(',', 1)[0]
        elif record is not None:
            record += line + '\n'

    if record is not None and citation_key in used_citations:
        new_bib_contents += record

    with open(out_path, 'w') as f:
        f.write(new_bib_contents)

# 使用方法：
remove_unused_references('new0403.aux', 'old.bib', 'new.bib')
