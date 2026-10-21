# FileTaxonomyTermTestCase::createAttachFileField()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 279–303 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L279-L303)
- **Class:** [FileTaxonomyTermTestCase](../FileTaxonomyTermTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
protected function createAttachFileField($name, $uri_scheme)
```

## Documentation

```text
Creates a file field and attaches it to the "Tags" taxonomy vocabulary.

@param $name
  The field name of the file field to create.
@param $uri_scheme
  The URI scheme to use for the file field (for example, "private" to
  create a field that stores private files or "public" to create a field
  that stores public files).
```

## Code

```php
  protected function createAttachFileField($name, $uri_scheme) {
    $field = array(
      'field_name' => $name,
      'type' => 'file',
      'settings' => array(
        'uri_scheme' => $uri_scheme,
      ),
      'cardinality' => 1,
    );
    field_create_field($field);
    // Attach an instance of it.
    $instance = array(
      'field_name' => $name,
      'label' => 'File',
      'entity_type' => 'taxonomy_term',
      'bundle' => 'tags',
      'required' => FALSE,
      'settings' => array(),
      'widget' => array(
        'type' => 'file_generic',
        'settings' => array(),
      ),
    );
    field_create_instance($instance);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
