# DatabaseCondition::mapConditionOperator()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1971–2004 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1971-L2004)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function mapConditionOperator($operator)
```

## Documentation

```text
Gets any special processing requirements for the condition operator.

Some condition types require special processing, such as IN, because
the value data they pass in is not a simple value. This is a simple
overridable lookup function.

@param $operator
  The condition operator, such as "IN", "BETWEEN", etc. Case-sensitive.

@return
  The extra handling directives for the specified operator, or NULL.
```

## Code

```php
  protected function mapConditionOperator($operator) {
    // $specials does not use drupal_static as its value never changes.
    static $specials = array(
      'BETWEEN' => array('delimiter' => ' AND '),
      'IN' => array('delimiter' => ', ', 'prefix' => ' (', 'postfix' => ')'),
      'NOT IN' => array('delimiter' => ', ', 'prefix' => ' (', 'postfix' => ')'),
      'EXISTS' => array('prefix' => ' (', 'postfix' => ')'),
      'NOT EXISTS' => array('prefix' => ' (', 'postfix' => ')'),
      'IS NULL' => array('use_value' => FALSE),
      'IS NOT NULL' => array('use_value' => FALSE),
      // Use backslash for escaping wildcard characters.
      'LIKE' => array('postfix' => " ESCAPE '\\\\'"),
      'NOT LIKE' => array('postfix' => " ESCAPE '\\\\'"),
      // These ones are here for performance reasons.
      '=' => array(),
      '<' => array(),
      '>' => array(),
      '>=' => array(),
      '<=' => array(),
    );
    if (isset($specials[$operator])) {
      $return = $specials[$operator];
    }
    else {
      // We need to upper case because PHP index matches are case sensitive but
      // do not need the more expensive drupal_strtoupper because SQL statements are ASCII.
      $operator = strtoupper($operator);
      $return = isset($specials[$operator]) ? $specials[$operator] : array();
    }

    $return += array('operator' => $operator);

    return $return;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
