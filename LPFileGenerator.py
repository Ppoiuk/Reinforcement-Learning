class LPFileGenerator:
    @staticmethod
    def generate_lp_file(jobs, filename):
        lines = []

        # Objective Function
        lines.append("Maximize")
        objective_terms = []
        for idx, job in enumerate(jobs):
            job_id = f"E{idx}"
            term = f"{job['priority']} {job_id}"
            objective_terms.append(term)
        lines.append(" + ".join(objective_terms))
        lines.append("")

        #  Constraints
        lines.append("Subject To")
        for idx, job in enumerate(jobs):
            e_var = f"E{idx}"
            s_var = f"S{idx}"
            r = job['r']
            d = job['Di']
            c = job['C_max']

            lines.append(f"{r} <= {s_var}")
            lines.append(f"{s_var} + {c} {e_var} <= {r + d}")
        lines.append("")

        #  Variable
        lines.append("Binary")
        for idx in range(len(jobs)):
            lines.append(f"E{idx}")
        lines.append("")

        lines.append("General")
        for idx in range(len(jobs)):
            lines.append(f"S{idx}")
        lines.append("")

        lines.append("End")

        #  Write to file
        with open(filename, 'w') as f:
            for line in lines:
                f.write(line + '\n')
