def process_frames_and_text(output_base_folder, csv_file):
    data = pd.read_csv(csv_file)
    video_frames = collect_frame_paths(output_base_folder)
    output_data = []

    for video_name, frames in video_frames.items():
        # 获取视频对应的文本信息
        text_info = data.loc[data['VIDEO_ID'] == video_name, 'SENTENCE'].values[0]

        # 创建键值对
        entry = {
            'Key': video_name,
            'Value': {
                'name': video_name,
                'gloss': '',  # 如果有其他信息需要添加在这里
                'text': text_info,
                'length': len(frames),
                'imgs_path': frames
            }
        }
        output_data.append(entry)

    return output_data


def save_to_csv(output_data, output_csv):
    with open(output_csv, 'w', encoding='utf-8') as f:
        for entry in output_data:
            key = entry['Key']
            value = json.dumps(entry['Value'], ensure_ascii=False)
            f.write(f'{key},{value}\n')


# 示例用法
output_base_folder = r'D:\glossannotation\pythonProject1\extracted_frames'
csv_file = r'D:\glossannotation\pythonProject1\how2sign_realigned_train.csv'
output_csv = r'D:\glossannotation\pythonProject1\output_data.csv'

output_data = process_frames_and_text(output_base_folder, csv_file)
save_to_csv(output_data, output_csv)
