# UpdateQuery_sqlite::execute()

- **Type:** Method
- **File:** [`includes/database/sqlite/query.inc`](../_file.md), lines 69–99 · [local source](../../../../../../source/includes/database/sqlite/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc#L69-L99)
- **Class:** [UpdateQuery_sqlite](../UpdateQuery_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function execute()
```

## Documentation

_No docblock in source._

## Code

```php
  public function execute() {
    if (!empty($this->queryOptions['sqlite_return_matched_rows'])) {
      return parent::execute();
    }

    // Get the fields used in the update query.
    $fields = $this->expressionFields + $this->fields;

    // Add the inverse of the fields to the condition.
    $condition = new DatabaseCondition('OR');
    foreach ($fields as $field => $data) {
      if (is_array($data)) {
        // The field is an expression.
        $condition->where($field . ' <> ' . $data['expression']);
        $condition->isNull($field);
      }
      elseif (!isset($data)) {
        // The field will be set to NULL.
        $condition->isNotNull($field);
      }
      else {
        $condition->condition($field, $data, '<>');
        $condition->isNull($field);
      }
    }
    if (count($condition)) {
      $condition->compile($this->connection, $this);
      $this->condition->where((string) $condition, $condition->arguments());
    }
    return parent::execute();
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
