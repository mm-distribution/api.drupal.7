# openid_update_7000()

- **Type:** Function
- **File:** [`modules/openid/openid.install`](_file.md), lines 174–226 · [local source](../../../../source/modules/openid/openid.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.install#L174-L226)
- **Module/theme:** openid
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function openid_update_7000()
```

## Documentation

```text
Bind associations to their providers.
```

## Code

```php
function openid_update_7000() {
  db_drop_table('openid_association');

  $schema = array(
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
  db_create_table('openid_association', $schema);
}
```

---
_Drupal 7.103 · [modules/openid/openid.install](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.install) · Licensed GPL-2.0-or-later (see LICENSE)._
