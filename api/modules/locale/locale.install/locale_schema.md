# locale_schema()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 274–456 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L274-L456)
- **Module/theme:** locale
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function locale_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function locale_schema() {
  $schema['languages'] = array(
    'description' => 'List of all available languages in the system.',
    'fields' => array(
      'language' => array(
        'type' => 'varchar',
        'length' => 12,
        'not null' => TRUE,
        'default' => '',
        'description' => "Language code, e.g. 'de' or 'en-US'.",
      ),
      'name' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Language name in English.',
      ),
      'native' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Native language name.',
      ),
      'direction' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Direction of language (Left-to-Right = 0, Right-to-Left = 1).',
      ),
      'enabled' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Enabled flag (1 = Enabled, 0 = Disabled).',
      ),
      'plurals' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Number of plural indexes in this language.',
      ),
      'formula' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Plural formula in PHP code to evaluate to get plural indexes.',
      ),
      'domain' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Domain to use for this language.',
      ),
      'prefix' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Path prefix to use for this language.',
      ),
      'weight' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Weight, used in lists of languages.',
      ),
      'javascript' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Location of JavaScript translation file.',
      ),
    ),
    'primary key' => array('language'),
    'indexes' => array(
      'list' => array('weight', 'name'),
    ),
  );

  $schema['locales_source'] = array(
    'description' => 'List of English source strings.',
    'fields' => array(
      'lid' => array(
        'type' => 'serial',
        'not null' => TRUE,
        'description' => 'Unique identifier of this string.',
      ),
      'location' => array(
        'type' => 'text',
        'not null' => FALSE,
        'size' => 'big',
        'description' => 'Drupal path in case of online discovered translations or file path in case of imported strings.',
      ),
      'textgroup' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => 'default',
        'description' => 'A module defined group of translations, see hook_locale().',
      ),
      'source' => array(
        'type' => 'text',
        'mysql_type' => 'blob',
        'not null' => TRUE,
        'description' => 'The original string in English.',
      ),
      'context' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The context this string applies to.',
      ),
      'version' => array(
        'type' => 'varchar',
        'length' => 20,
        'not null' => TRUE,
        'default' => 'none',
        'description' => 'Version of Drupal, where the string was last used (for locales optimization).',
      ),
    ),
    'primary key' => array('lid'),
    'indexes' => array(
      'source_context' => array(array('source', 30), 'context'),
    ),
  );

  $schema['locales_target'] = array(
    'description' => 'Stores translated versions of strings.',
    'fields' => array(
      'lid' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Source string ID. References {locales_source}.lid.',
      ),
      'translation' => array(
        'type' => 'text',
        'mysql_type' => 'blob',
        'not null' => TRUE,
        'description' => 'Translation string value in this language.',
      ),
      'language' => array(
        'type' => 'varchar',
        'length' => 12,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Language code. References {languages}.language.',
      ),
      'plid' => array(
        'type' => 'int',
        'not null' => TRUE, // This should be NULL for no referenced string, not zero.
        'default' => 0,
        'description' => 'Parent lid (lid of the previous string in the plural chain) in case of plural strings. References {locales_source}.lid.',
      ),
      'plural' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Plural index number in case of plural strings.',
      ),
    ),
    'primary key' => array('language', 'lid', 'plural'),
    'foreign keys' => array(
      'locales_source' => array(
        'table' => 'locales_source',
        'columns' => array('lid' => 'lid'),
      ),
    ),
    'indexes' => array(
      'lid'      => array('lid'),
      'plid'     => array('plid'),
      'plural'   => array('plural'),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
