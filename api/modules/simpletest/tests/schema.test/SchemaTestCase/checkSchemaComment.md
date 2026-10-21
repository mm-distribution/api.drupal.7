# SchemaTestCase::checkSchemaComment()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 162–167 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L162-L167)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function checkSchemaComment($description, $table, $column = NULL)
```

## Documentation

```text
Checks that a table or column comment matches a given description.

@param $description
  The asserted description.
@param $table
  The table to test.
@param $column
  Optional column to test.
```

## Code

```php
  function checkSchemaComment($description, $table, $column = NULL) {
    if (method_exists(Database::getConnection()->schema(), 'getComment')) {
      $comment = Database::getConnection()->schema()->getComment($table, $column);
      $this->assertEqual($comment, $description, 'The comment matches the schema description.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
