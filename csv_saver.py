import csv


def save_rows_to_csv(filename, rows, header=None):
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows:
            writer.writerow(['{:.3f}'.format(v) for v in row])


def save_rows_to_latex(filename, rows, header=None):
    with open(filename, "wb") as f:
        if header is not None:
            for i, val in enumerate(header):
                f.write('{}'.format(val))
                if i < len(header) - 1:
                    f.write('&')
            f.write('\\\\ \\hline  \n')
        for j, row in enumerate(rows):
            for i, val in enumerate(row):
                f.write('\SI{{{}}}{{}}'.format(val))
                if i < len(row) - 1:
                    f.write('&')
            if j < len(rows) - 1:
                f.write('\\\\\n')
