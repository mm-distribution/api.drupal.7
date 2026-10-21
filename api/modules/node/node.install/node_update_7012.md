# node_update_7012()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 886–913 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L886-L913)
- **Module/theme:** node
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function node_update_7012()
```

## Documentation

```text
Switches body fields to untranslatable while upgrading from D6 and makes them language neutral.
```

## Code

```php
function node_update_7012() {
  // If we are upgrading from D6, then body fields should be set back to
  // untranslatable, as D6 did not know about the idea of translating fields,
  // but only nodes. If a D7 > D7 update is running we need to skip this update,
  // as it is a valid use case to have translatable body fields in this context.
  if (variable_get('update_d6', FALSE)) {
    // Make node bodies untranslatable: field_update_field() cannot be used
    // throughout the upgrade process and we do not have an update counterpart
    // for _update_7000_field_create_field(). Hence we are forced to update the
    // 'field_config' table directly. This is a safe operation since it is
    // being performed while upgrading from D6. Perfoming the same operation
    // during a D7 update is highly discouraged.
    db_update('field_config')
      ->fields(array('translatable' => 0))
      ->condition('field_name', 'body')
      ->execute();

    // Switch field languages to LANGUAGE_NONE, since initially they were
    // assigned the node language.
    foreach (array('field_data_body', 'field_revision_body') as $table) {
      db_update($table)
        ->fields(array('language' => LANGUAGE_NONE))
        ->execute();
    }

    node_type_cache_reset();
  }
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
