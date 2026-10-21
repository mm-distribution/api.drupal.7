# user_schema()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 11–298 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L11-L298)
- **Module/theme:** user
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function user_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function user_schema() {
  $schema['authmap'] = array(
    'description' => 'Stores distributed authentication mapping.',
    'fields' => array(
      'aid' => array(
        'description' => 'Primary Key: Unique authmap ID.',
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'uid' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => "User's {users}.uid.",
      ),
      'authname' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Unique authentication name.',
      ),
      'module' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Module which is controlling the authentication.',
      ),
    ),
    'unique keys' => array(
      'authname' => array('authname'),
    ),
    'primary key' => array('aid'),
    'foreign keys' => array(
      'user' => array(
        'table' => 'users',
        'columns' => array('uid' => 'uid'),
      ),
    ),
    'indexes' => array(
      'uid_module' => array('uid', 'module'),
    ),
  );

  $schema['role_permission'] = array(
    'description' => 'Stores the permissions assigned to user roles.',
    'fields' => array(
      'rid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => 'Foreign Key: {role}.rid.',
      ),
      'permission' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'A single permission granted to the role identified by rid.',
      ),
      'module' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => "The module declaring the permission.",
      ),
    ),
    'primary key' => array('rid', 'permission'),
    'indexes' => array(
      'permission' => array('permission'),
    ),
    'foreign keys' => array(
      'role' => array(
        'table' => 'role',
        'columns' => array('rid' => 'rid'),
      ),
    ),
  );

  $schema['role'] = array(
    'description' => 'Stores user roles.',
    'fields' => array(
      'rid' => array(
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => 'Primary Key: Unique role ID.',
      ),
      'name' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Unique role name.',
        'translatable' => TRUE,
      ),
      'weight' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The weight of this role in listings and the user interface.',
      ),
    ),
    'unique keys' => array(
      'name' => array('name'),
    ),
    'primary key' => array('rid'),
    'indexes' => array(
      'name_weight' => array('name', 'weight'),
    ),
  );

  // The table name here is plural, despite Drupal table naming standards,
  // because "user" is a reserved word in many databases.
  $schema['users'] = array(
    'description' => 'Stores user data.',
    'fields' => array(
      'uid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => 'Primary Key: Unique user ID.',
        'default' => 0,
      ),
      'name' => array(
        'type' => 'varchar',
        'length' => 60,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Unique user name.',
      ),
      'pass' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => "User's password (hashed).",
      ),
      'mail' => array(
        'type' => 'varchar',
        'length' => 254,
        'not null' => FALSE,
        'default' => '',
        'description' => "User's e-mail address.",
      ),
      'theme' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => "User's default theme.",
      ),
      'signature' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => "User's signature.",
      ),
      'signature_format' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => FALSE,
        'description' => 'The {filter_format}.format of the signature.',
      ),
      'created' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Timestamp for when user was created.',
      ),
      'changed' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Timestamp for when user was changed.',
      ),
      'access' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Timestamp for previous time user accessed the site.',
      ),
      'login' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => "Timestamp for user's last login.",
      ),
      'status' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'size' => 'tiny',
        'description' => 'Whether the user is active(1) or blocked(0).',
      ),
      'timezone' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => FALSE,
        'description' => "User's time zone.",
      ),
      'language' => array(
        'type' => 'varchar',
        'length' => 12,
        'not null' => TRUE,
        'default' => '',
        'description' => "User's default language.",
      ),
      'picture' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => "Foreign key: {file_managed}.fid of user's picture.",
      ),
      'init' => array(
        'type' => 'varchar',
        'length' => 254,
        'not null' => FALSE,
        'default' => '',
        'description' => 'E-mail address used for initial account creation.',
      ),
      'data' => array(
        'type' => 'blob',
        'not null' => FALSE,
        'size' => 'big',
        'serialize' => TRUE,
        'description' => 'A serialized array of name value pairs that are related to the user. Any form values posted during user edit are stored and are loaded into the $user object during user_load(). Use of this field is discouraged and it will likely disappear in a future version of Drupal.',
      ),
    ),
    'indexes' => array(
      'access' => array('access'),
      'created' => array('created'),
      'changed' => array('changed'),
      'mail' => array('mail'),
      'picture' => array('picture'),
    ),
    'unique keys' => array(
      'name' => array('name'),
    ),
    'primary key' => array('uid'),
    'foreign keys' => array(
      'signature_format' => array(
        'table' => 'filter_format',
        'columns' => array('signature_format' => 'format'),
      ),
    ),
  );

  $schema['users_roles'] = array(
    'description' => 'Maps users to roles.',
    'fields' => array(
      'uid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Primary Key: {users}.uid for user.',
      ),
      'rid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Primary Key: {role}.rid for role.',
      ),
    ),
    'primary key' => array('uid', 'rid'),
    'indexes' => array(
      'rid' => array('rid'),
    ),
    'foreign keys' => array(
      'user' => array(
        'table' => 'users',
        'columns' => array('uid' => 'uid'),
      ),
      'role' => array(
        'table' => 'role',
        'columns' => array('rid' => 'rid'),
      ),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
