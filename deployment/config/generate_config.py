import argparse
import logging
import json

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('config_file', help='Config file to save parameters')

    parser.add_argument('--project_id', help='Your Project ID.', required=True)

    parser.add_argument('--osm_url', help='URL of the source OSM file', required=True)
    parser.add_argument('--osm_md5_url', help='URL of the source OSM file\'s MD5 hash', required=True)

    parser.add_argument('--gcs_transfer_bucket', help='GCS bucket to make transferring source file to project\'s GCS',
                        required=True)
    parser.add_argument('--transfer_index_files_gcs_uri', help='GCS URI to Storage Transfer index file',
                        required=True)

    parser.add_argument('--json_results_gcs_uri', help='GCS URI to store results JSON files', required=True)

    parser.add_argument('--osm_to_features_image', help='osm_to_features image name', required=True)
    parser.add_argument('--osm_to_nodes_ways_relations_image', help='osm_to_nodes_ways_relations image name',
                        required=True)
    parser.add_argument('--generate_layers_image', help='generate_layers image name', required=True)

    parser.add_argument('--osm_to_features_gke_pool', help='osm_to_features GKE pool name', required=True)
    parser.add_argument('--osm_to_features_gke_pod_requested_memory', help='osm_to_features GKE POD requested memory',
                        required=True)
    parser.add_argument('--additional_gke_pool', help='GKE pool name for additional operations',
                        required=True)
    parser.add_argument('--additional_gke_pool_pod_max_num_treads',
                        help='Maximum numbers of threads that can be used on the additional GKE pool pod',
                        required=True)

    parser.add_argument('--bq_dataset_to_export', help='BigQuery dataset name to export results', required=True)

    args = parser.parse_args()
    args_filtered = {}
    for k, v in vars(args).items():
        if v:
            print(v)
            args_filtered[k] = v

    with open(args.config_file, 'w') as fp:
        json.dump(args_filtered, fp, indent=4)

