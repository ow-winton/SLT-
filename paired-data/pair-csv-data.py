import os
import pandas as pd
import json


def collect_frame_paths(output_base_folder):
    video_frames = {}

    for video_name in os.listdir(output_base_folder):
        video_folder = os.path.join(output_base_folder, video_name)
        if os.path.isdir(video_folder):
            frames = sorted(
                [os.path.join(video_folder, frame) for frame in os.listdir(video_folder) if frame.endswith('.jpg')])
            # 将绝对路径转换为相对路径
            relative_frames = [os.path.relpath(frame, output_base_folder) for frame in frames]
            video_frames[video_name] = relative_frames

    return video_frames


def process_frames_and_text(output_base_folder, csv_file):
    # 读取 CSV 文件，指定分隔符为制表符
    data = pd.read_csv(csv_file, sep='\t')

    video_frames = collect_frame_paths(output_base_folder)
    output_data = []

    for video_name, frames in video_frames.items():
        # 尝试找到对应的文本信息
        matching_rows = data.loc[data['SENTENCE_NAME'] == video_name, 'SENTENCE']
        if len(matching_rows) == 0:
            print(f"Warning: No matching record found for video {video_name}")
            continue

        text_info = matching_rows.values[0]

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
    # 确保输出目录存在
    output_dir = os.path.dirname(output_csv)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_csv, 'w', encoding='utf-8') as f:
        for entry in output_data:
            key = entry['Key']
            value = json.dumps(entry['Value'], ensure_ascii=False)
            f.write(f'{key},{value}\n')
# 示例用法
output_base_folder = r'D:\glossannotation\pythonProject1\clip\output'
csv_file = r'D:\glossannotation\pythonProject1\paired-data\how2sign_realigned_train.csv'
output_csv = r'D:\glossannotation\pythonProject1\paired-data\output\output_data.csv'

output_data = process_frames_and_text(output_base_folder, csv_file)
save_to_csv(output_data, output_csv)
