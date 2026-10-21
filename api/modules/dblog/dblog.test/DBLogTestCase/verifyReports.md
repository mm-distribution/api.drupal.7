# DBLogTestCase::verifyReports()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 202–239 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L202-L239)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function verifyReports($response = 200)
```

## Documentation

```text
Confirms that database log reports are displayed at the correct paths.

@param int $response
  (optional) HTTP response code. Defaults to 200.
```

## Code

```php
  private function verifyReports($response = 200) {
    $quote = '&#039;';

    // View the database log help page.
    $this->drupalGet('admin/help/dblog');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Database logging'), 'DBLog help was displayed');
    }

    // View the database log report page.
    $this->drupalGet('admin/reports/dblog');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Recent log messages'), 'DBLog report was displayed');
    }

    // View the database log page-not-found report page.
    $this->drupalGet('admin/reports/page-not-found');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Top ' . $quote . 'page not found' . $quote . ' errors'), 'DBLog page-not-found report was displayed');
    }

    // View the database log access-denied report page.
    $this->drupalGet('admin/reports/access-denied');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Top ' . $quote . 'access denied' . $quote . ' errors'), 'DBLog access-denied report was displayed');
    }

    // View the database log event page.
    $this->drupalGet('admin/reports/event/1');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Details'), 'DBLog event node was displayed');
    }
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
