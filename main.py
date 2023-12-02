from sonar_rules_exporter import export_multiple_languages

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    languages = ['plsql', 'tsql', 'JavaScript', 'Python', 'PHP', 'Java', 'html']
    export_multiple_languages(languages)

    print("successfully!")
