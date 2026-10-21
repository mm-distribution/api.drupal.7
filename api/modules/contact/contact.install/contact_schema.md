# contact_schema()

- **Type:** Function
- **File:** [`modules/contact/contact.install`](_file.md), lines 11–65 · [local source](../../../../source/modules/contact/contact.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install#L11-L65)
- **Module/theme:** contact
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function contact_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function contact_schema() {
  $schema['contact'] = array(
    'description' => 'Contact form category settings.',
    'fields' => array(
      'cid' => array(
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => 'Primary Key: Unique category ID.',
      ),
      'category' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Category name.',
        'translatable' => TRUE,
      ),
      'recipients' => array(
        'type' => 'text',
        'not null' => TRUE,
        'size' => 'big',
        'description' => 'Comma-separated list of recipient e-mail addresses.',
      ),
      'reply' => array(
        'type' => 'text',
        'not null' => TRUE,
        'size' => 'big',
        'description' => 'Text of the auto-reply message.',
      ),
      'weight' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => "The category's weight.",
      ),
      'selected' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'size' => 'tiny',
        'description' => 'Flag to indicate whether or not category is selected by default. (1 = Yes, 0 = No)',
      ),
    ),
    'primary key' => array('cid'),
    'unique keys' => array(
      'category' => array('category'),
    ),
    'indexes' => array(
      'list' => array('weight', 'category'),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/contact/contact.install](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install) · Licensed GPL-2.0-or-later (see LICENSE)._
