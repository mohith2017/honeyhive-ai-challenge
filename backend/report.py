import pandas as pd

def generate_report(results):
  df = pd.DataFrame(results)
  styled_df = df.style.set_table_styles([
      {'selector': 'table', 'props': [('border', '1px solid black')]},
      {'selector': 'th', 'props': [('background-color', '#ddd'), ('color', 'black')]},
      {'selector': 'td', 'props': [('text-align', 'left')]}
  ])
  # Generate the report
  report = styled_df.render()
  return report


# print(generate_report(compute_metrics))