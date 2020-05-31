def get_rdv_str(rendezvous_infos):
  return ''.join([info + ';' for info in rendezvous_infos.values()])


def add_rendezvous(rendezvous_infos):
  rendervous_file = open('./files/rendervous.txt', 'a')
  rdv_str = get_rdv_str(rendezvous_infos)

  rendervous_file.write(rdv_str + '\n')
  rendervous_file.close()
