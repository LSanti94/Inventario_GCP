import subprocess
import csv

# Función para ejecutar comandos de gcloud y capturar la salida
def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip().splitlines()

# Función para obtener la lista de proyectos de GCP
def obtener_lista_proyectos():
    result = subprocess.run('gcloud projects list --format="value(projectId)"', capture_output=True, text=True, shell=True)
    proyectos = result.stdout.strip().split("\n")
    return proyectos

# Función para seleccionar el proyecto por nombre
def seleccionar_proyecto(proyectos):
    print("Proyectos disponibles:")
    for proyecto in proyectos:
        print(proyecto)
    
    while True:
        seleccion = input("Ingresa el nombre del proyecto con el que deseas trabajar: ").strip()
        if seleccion in proyectos:
            return seleccion
        else:
            print("Nombre de proyecto no válido. Por favor, intenta nuevamente.")

# Función para listar VMs
def list_vm(output_file, project):
    vm_command = f'gcloud compute instances list --project {project} --format="csv(NAME,ZONE,INTERNAL_IP,EXTERNAL_IP,STATUS)"'
    vm_data = execute_command(vm_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["VMs"])
        writer.writerows(csv.reader(vm_data))
        writer.writerow([])

# Función para listar discos
def list_disks(output_file, project):
    disk_command = f'gcloud compute disks list --project {project} --format="csv(name,location,users)"'
    disk_data = execute_command(disk_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Discos"])
        writer.writerows(csv.reader(disk_data))
        writer.writerow([])

# Función para listar buckets
def list_buckets(output_file, project):
    buckets_command = f'gsutil ls -p {project}'
    buckets_data = execute_command(buckets_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Buckets"])
        writer.writerows(csv.reader(buckets_data))
        writer.writerow([])

# Función para listar Clusters
def list_clusters(output_file, project):
    clusters_command = f'gcloud container clusters list --project {project} --format="csv(name,status)"'
    clusters_data = execute_command(clusters_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Clusters"])
        writer.writerows(csv.reader(clusters_data))
        writer.writerow([])

# Función para listar App Engine Versiones
def list_app_engine_versions(output_file, project):
    App_Engine_command = f'gcloud app versions list --project {project} --format="csv(name,status)"'
    App_Engine_data = execute_command(App_Engine_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["App-Engine-Versiones"])
        writer.writerows(csv.reader(App_Engine_data))
        writer.writerow([])

# Función para listar BigQuery API
def list_bigquery_api(output_file, project):
    BigQuery_API_command = f'bq ls --project {project}'
    BigQuery_API_data = execute_command(BigQuery_API_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["BigQuery-API"])
        writer.writerows(csv.reader(BigQuery_API_data))
        writer.writerow([])

# Función para listar Cloud Functions API
def list_functions_api(output_file, project):
    Cloud_Functions_API_command = f'gcloud functions list --project {project} --format="csv(NAME,STATE,REGION)"'
    Cloud_Functions_API_data = execute_command(Cloud_Functions_API_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Cloud-Functions-API-data"])
        writer.writerows(csv.reader(Cloud_Functions_API_data))
        writer.writerow([])

# Función para listar scheduler jobs
def list_scheduler_jobs(output_file, project):
    scheduler_jobs_command = f'gcloud scheduler jobs list --project {project} --format="csv(ID,LOCATION,TARGET_TYPE,STATE)"'
    scheduler_jobs_command_data = execute_command(scheduler_jobs_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Scheduler-Jobs"])
        writer.writerows(csv.reader(scheduler_jobs_command_data))
        writer.writerow([])

# Función para listar Container Registry API
def list_cr_api(output_file, project):
    Container_Registry_APIcommand = f'gcloud container images list --project {project}'
    Container_Registry_API_data = execute_command(Container_Registry_APIcommand)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Container-Registry-API"])
        writer.writerows(csv.reader(Container_Registry_API_data))
        writer.writerow([])

# Función para listar DNS
def list_dns(output_file, project):
    dns_command = f'gcloud dns managed-zones list --project {project}'
    dns_data = execute_command(dns_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["DNS"])
        writer.writerows(csv.reader(dns_data))
        writer.writerow([])

# Función para listar Cloud Pub/Sub API
def list_ps_api(output_file, project):
    Pub_Sub_API_API_command = f'gcloud pubsub topics list --project {project} --format="csv(NAME)"'
    Pub_Sub_API_data = execute_command(Pub_Sub_API_API_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Cloud-Pub/Sub-API"])
        writer.writerows(csv.reader(Pub_Sub_API_data))
        writer.writerow([])

# Función para listar App Engine
def list_app_engine(output_file, project):
    App_Engine_command = f'gcloud app services list --project {project}'
    App_Engine_data = execute_command(App_Engine_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["App-Engine"])
        writer.writerows(csv.reader(App_Engine_data))
        writer.writerow([])

# Función para listar Cloud Datastore NoSQL
def list_datastore(output_file, project):
    Datastore_NoSQL_command = f'gcloud datastore indexes list --project {project}'
    Datastore_NoSQL_data = execute_command(Datastore_NoSQL_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Datastore_NoSQL"])
        writer.writerows(csv.reader(Datastore_NoSQL_data))
        writer.writerow([])

# Función para habilitar la API SQL con confirmación del usuario
def habilitar_api_sql(project):
    print(f"¿Deseas habilitar la API de SQL Admin para el proyecto {project}?")
    confirmacion = input("(y/N): ").strip().lower()
    if confirmacion == 'y':
        command = f'gcloud services enable sqladmin.googleapis.com --project {project}'
        execute_command(command)
        print("API de SQL Admin habilitada.")
        return True
    else:
        print("No se habilitó la API de SQL Admin. El script no podrá listar las instancias SQL.")
        return False

# Función para listar SQL
def list_SQL(output_file, project):
    SQL_command = f'gcloud sql instances list --project {project} --format="csv(name,state)"'
    SQL_data = execute_command(SQL_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["SQL"])
        writer.writerows(csv.reader(SQL_data))
        writer.writerow([])

# Función para habilitar la API de Spanner con confirmación del usuario
def habilitar_api_spanner(project):
    print(f"¿Deseas habilitar la API de Spanner para el proyecto {project}?")
    confirmacion = input("(y/N): ").strip().lower()
    if confirmacion == 'y':
        command = f'gcloud services enable spanner.googleapis.com --project {project}'
        execute_command(command)
        print("API de Spanner habilitada.")
        return True
    else:
        print("No se habilitó la API de Spanner. El script no podrá listar las instancias de Spanner.")
        return False


# Función para listar DB relacionales global
def list_db_relacionales_global(output_file, project):
    DB_relacionales_global_command = f'gcloud spanner instances list --project {project}'
    DB_relacionales_global_data = execute_command(DB_relacionales_global_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["DB_relacionales_global_data"])
        writer.writerows(csv.reader(DB_relacionales_global_data))
        writer.writerow([])


# Función para listar Cloud Firestore
def list_firestore(output_file, project):
    firestore_command = f'gcloud firestore databases list --project {project}'
    firestore_data = execute_command(firestore_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Firestore"])
        writer.writerows(csv.reader(firestore_data))
        writer.writerow([])

# Función para listar VPC
def list_VPC(output_file, project):
    vpc_command = f'gcloud compute networks list --project {project}'
    vpc_data = execute_command(vpc_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["VPC"])
        writer.writerows(csv.reader(vpc_data))
        writer.writerow([])

# Función para listar LB
def list_lb(output_file, project):
    LB_command = f'gcloud compute target-pools list --project {project} --format="csv(NAME,REGION, HEALTH_CHECKS)"'
    LB_data = execute_command(LB_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["LB"])
        writer.writerows(csv.reader(LB_data))
        writer.writerow([])

# Función para listar CDN
def list_cdn(output_file, project):
    CDN_command = f'gcloud compute backend-services list --project {project} --format="csv(NAME, PROTOCOL)"'
    CDN_data = execute_command(CDN_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["CDN"])
        writer.writerows(csv.reader(CDN_data))
        writer.writerow([])

# Función para listar Security scanner
def list_sec_scanner(output_file, project):
    sec_scanner_command = f'gcloud beta compute security-scans list --project {project}'
    sec_scanner_data = execute_command(sec_scanner_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["sec_scanner"])
        writer.writerows(csv.reader(sec_scanner_data))
        writer.writerow([])

# Función para listar Armor
def list_armor(output_file, project):
    armor_command = f'gcloud compute security-policies list --project {project}'
    armor_data = execute_command(armor_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Armor"])
        writer.writerows(csv.reader(armor_data))
        writer.writerow([])

# Función para listar Monitoring
def list_monitoring(output_file, project):
    monitoring_command = f'gcloud monitoring dashboards list --project {project} --format="csv(NAME)"'
    monitoring_data = execute_command(monitoring_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Monitoreo"])
        writer.writerows(csv.reader(monitoring_data))
        writer.writerow([])

# Función para listar Deployment Manager
def list_deploy_manager(output_file, project):
    deploy_manager_command = f'gcloud deployment-manager deployments list --project {project} --format="csv(NAME,STATUS,ERRORS)"'
    deploy_manager_data = execute_command(deploy_manager_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Deployment-Manager"])
        writer.writerows(csv.reader(deploy_manager_data))
        writer.writerow([])

# Función para habilitar la API de Cloud Tasks con confirmación del usuario
def habilitar_api_tasks(project):
    print(f"¿Deseas habilitar la API de Cloud Tasks para el proyecto {project}?")
    confirmacion = input("(y/N): ").strip().lower()
    if confirmacion == 'y':
        command = f'gcloud services enable cloudtasks.googleapis.com --project {project}'
        execute_command(command)
        print("API de Cloud Tasks habilitada.")
        return True
    else:
        print("No se habilitó la API de Cloud Tasks. El script no podrá listar las tareas.")
        return False


# Función para listar Tasks
def list_tasks(output_file, project):
    tasks_command = f'gcloud tasks queues list --project {project}'
    tasks_data = execute_command(tasks_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Tasks"])
        writer.writerows(csv.reader(tasks_data))
        writer.writerow([])

# Función para listar build
def list_build(output_file, project):
    build_command = f'gcloud builds list --project {project} --format="csv(ID,CREATE_TIME,SOURCE,STATUS)"'
    build_data = execute_command(build_command)
    with open(output_file, "a", newline='') as file:
        writer = csv.writer(file, delimiter='\t')  # Usar delimitador de pestaña
        writer.writerow(["Build"])
        writer.writerows(csv.reader(build_data))
        writer.writerow([])

# Ejecutar listado de VMs, discos, buckets
def ejecutar_listados(output_file, project):
    list_vm(output_file, project); list_disks(output_file, project); list_buckets(output_file, project); list_clusters(output_file, project); list_app_engine_versions(output_file, project); list_bigquery_api(output_file, project); list_functions_api(output_file, project); list_scheduler_jobs(output_file, project); list_cr_api(output_file, project); list_dns(output_file, project); list_ps_api(output_file, project); list_functions_api(output_file, project); list_app_engine(output_file, project); list_datastore(output_file, project); habilitar_api_sql(project); list_SQL(output_file, project); habilitar_api_spanner(project); list_db_relacionales_global(output_file, project); list_firestore(output_file, project); list_VPC(output_file, project); list_lb(output_file, project); list_cdn(output_file, project); list_sec_scanner(output_file, project); list_armor(output_file, project); list_monitoring(output_file, project); list_deploy_manager(output_file, project); habilitar_api_tasks(project); list_tasks(output_file, project); list_build(output_file, project)

# Obtener y seleccionar el proyecto
proyectos = obtener_lista_proyectos()
proyecto_seleccionado = seleccionar_proyecto(proyectos)

# Nombre del archivo CSV
OUTPUT_FILE = f"recursos_gcp_{proyecto_seleccionado}.csv"

# Ejecutar listado de recursos para el proyecto seleccionado
ejecutar_listados(OUTPUT_FILE, proyecto_seleccionado)

print(f"Los datos se han guardado en {OUTPUT_FILE}.")
