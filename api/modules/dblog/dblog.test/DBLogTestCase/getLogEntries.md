# DBLogTestCase::getLogEntries()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 608–622 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L608-L622)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
protected function getLogEntries()
```

## Documentation

```text
Gets the database log event information from the browser page.

@return array
  List of log events where each event is an array with following keys:
  - severity: (int) A database log severity constant.
  - type: (string) The type of database log event.
  - message: (string) The message for this database log event.
  - user: (string) The user associated with this database log event.
```

## Code

```php
  protected function getLogEntries() {
    $entries = array();
    if ($table = $this->xpath('.//table[@id="admin-dblog"]')) {
      $table = array_shift($table);
      foreach ($table->tbody->tr as $row) {
        $entries[] = array(
          'severity' => $this->getSeverityConstant($row['class']),
          'type' => $this->asText($row->td[1]),
          'message' => $this->asText($row->td[3]),
          'user' => $this->asText($row->td[4]),
        );
      }
    }
    return $entries;
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
