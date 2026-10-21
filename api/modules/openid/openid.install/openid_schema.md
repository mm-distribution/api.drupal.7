# openid_schema()

- **Type:** Function
- **File:** [`modules/openid/openid.install`](_file.md), lines 11–88 · [local source](../../../../source/modules/openid/openid.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.install#L11-L88)
- **Module/theme:** openid
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function openid_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function openid_schema() {
  $schema['openid_association'] = array(
    'description' => 'Stores temporary shared key association information for OpenID authentication.',
    'fields' => array(
      'idp_endpoint_uri' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'description' => 'Primary Key: URI of the OpenID Provider endpoint.',
      ),
      'assoc_handle' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'description' => 'Used to refer to this association in subsequent messages.',
      ),
      'assoc_type' => array(
        'type' => 'varchar',
        'length' => 32,
        'description' => 'The signature algorithm used: one of HMAC-SHA1 or HMAC-SHA256.',
      ),
      'session_type' => array(
        'type' => 'varchar',
        'length' => 32,
        'description' => 'Valid association session types: "no-encryption", "DH-SHA1", and "DH-SHA256".',
      ),
      'mac_key' => array(
        'type' => 'varchar',
        'length' => 255,
        'description' => 'The MAC key (shared secret) for this association.',
      ),
      'created' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'UNIX timestamp for when the association was created.',
      ),
      'expires_in' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The lifetime, in seconds, of this association.',
      ),
    ),
    'primary key' => array('idp_endpoint_uri'),
    'unique keys' => array(
      'assoc_handle' => array('assoc_handle'),
    ),
  );

  $schema['openid_nonce'] = array(
    'description' => 'Stores received openid.response_nonce per OpenID endpoint URL to prevent replay attacks.',
    'fields' => array(
      'idp_endpoint_uri' => array(
        'type' => 'varchar',
        'length' => 255,
        'description' => 'URI of the OpenID Provider endpoint.',
      ),
      'nonce' => array(
        'type' => 'varchar',
        'length' => 255,
        'description' => 'The value of openid.response_nonce.',
      ),
      'expires' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'A Unix timestamp indicating when the entry should expire.',
      ),
    ),
    'indexes' => array(
      'nonce' => array('nonce'),
      'expires' => array('expires'),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/openid/openid.install](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.install) · Licensed GPL-2.0-or-later (see LICENSE)._
