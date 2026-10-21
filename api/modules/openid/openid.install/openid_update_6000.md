# openid_update_6000()

- **Type:** Function
- **File:** [`modules/openid/openid.install`](_file.md), lines 132–160 · [local source](../../../../source/modules/openid/openid.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.install#L132-L160)
- **Module/theme:** openid
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function openid_update_6000()
```

## Documentation

```text
Add a table to store nonces.
```

## Code

```php
function openid_update_6000() {
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
        'description' => 'The value of openid.response_nonce'
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

  db_create_table('openid_nonce', $schema['openid_nonce']);
}
```

---
_Drupal 7.103 · [modules/openid/openid.install](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.install) · Licensed GPL-2.0-or-later (see LICENSE)._
