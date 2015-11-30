import xmlrpclib
import sys


def create_wordpress_page(title, content, publish):
    wp_url = 'http://wordpress.bigdecisions.loc/xmlrpc.php'
    wp_user = 'admin'
    wp_pass = 'admin'
    blog_id = ""
    publish = 1 if publish else 'draft'
    server = xmlrpclib.ServerProxy(wp_url)
    
    payload = {
        'title': title,
        'type': 'post',
        'description': ''.join(content)
    }
    print content
    post_id = server.metaWeblog.newPost(blog_id,wp_user,wp_pass,payload,publish)
    return post_id 


if __name__ == '__main__':
   if len(sys.argv) != 2:
      print "Usage: {} input-text-file".format(sys.argv[0])
      sys.exit(1)
   with open(sys.argv[1]) as f:
      content = f.readlines()
      title = content[0].strip() 
   create_wordpress_page(title, content, True)
