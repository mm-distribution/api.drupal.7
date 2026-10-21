# StatisticsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 14–46 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L14-L46)
- **Class:** [StatisticsTestCase](../StatisticsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('statistics');

    // Create user.
    $this->blocking_user = $this->drupalCreateUser(array(
      'access administration pages',
      'access site reports',
      'access statistics',
      'block IP addresses',
      'administer blocks',
      'administer statistics',
      'administer users',
    ));
    $this->drupalLogin($this->blocking_user);

    // Enable access logging.
    variable_set('statistics_enable_access_log', 1);
    variable_set('statistics_count_content_views', 1);

    // Insert dummy access by anonymous user into access log.
    db_insert('accesslog')
      ->fields(array(
        'title' => 'test',
        'path' => 'node/1',
        'url' => 'http://example.com',
        'hostname' => '1.2.3.3',
        'uid' => 0,
        'sid' => 10,
        'timer' => 10,
        'timestamp' => REQUEST_TIME,
      ))
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
