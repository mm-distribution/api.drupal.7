# SchemaTestCase::testSchemaAddField()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 226–293 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L226-L293)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSchemaAddField()
```

## Documentation

```text
Test adding columns to an existing table.
```

## Code

```php
  function testSchemaAddField() {
    // Test varchar types.
    foreach (array(1, 32, 128, 256, 512) as $length) {
      $base_field_spec = array(
        'type' => 'varchar',
        'length' => $length,
      );
      $variations = array(
        array('not null' => FALSE),
        array('not null' => FALSE, 'default' => '7'),
        array('not null' => TRUE, 'initial' => 'd'),
        array('not null' => TRUE, 'initial' => 'd', 'default' => '7'),
      );

      foreach ($variations as $variation) {
        $field_spec = $variation + $base_field_spec;
        $this->assertFieldAdditionRemoval($field_spec);
      }
    }

    // Test int and float types.
    foreach (array('int', 'float') as $type) {
      foreach (array('tiny', 'small', 'medium', 'normal', 'big') as $size) {
        $base_field_spec = array(
          'type' => $type,
          'size' => $size,
        );
        $variations = array(
          array('not null' => FALSE),
          array('not null' => FALSE, 'default' => 7),
          array('not null' => TRUE, 'initial' => 1),
          array('not null' => TRUE, 'initial' => 1, 'default' => 7),
        );

        foreach ($variations as $variation) {
          $field_spec = $variation + $base_field_spec;
          $this->assertFieldAdditionRemoval($field_spec);
        }
      }
    }

    // Test numeric types.
    foreach (array(1, 5, 10, 40, 65) as $precision) {
      foreach (array(0, 2, 10, 30) as $scale) {
        if ($precision <= $scale) {
          // Precision must be smaller then scale.
          continue;
        }

        $base_field_spec = array(
          'type' => 'numeric',
          'scale' => $scale,
          'precision' => $precision,
        );
        $variations = array(
          array('not null' => FALSE),
          array('not null' => FALSE, 'default' => 7),
          array('not null' => TRUE, 'initial' => 1),
          array('not null' => TRUE, 'initial' => 1, 'default' => 7),
        );

        foreach ($variations as $variation) {
          $field_spec = $variation + $base_field_spec;
          $this->assertFieldAdditionRemoval($field_spec);
        }
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
