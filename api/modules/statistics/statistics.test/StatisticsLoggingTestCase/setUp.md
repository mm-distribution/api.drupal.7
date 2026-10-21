# StatisticsLoggingTestCase::setUp()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 67–85 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L67-L85)
- **Class:** [StatisticsLoggingTestCase](../StatisticsLoggingTestCase.md)
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

    $this->auth_user = $this->drupalCreateUser(array('access content', 'create page content', 'edit own page content'));

    // Ensure we have a node page to access.
    $this->node = $this->drupalCreateNode(array('title' => $this->randomName(255), 'uid' => $this->auth_user->uid));

    // Enable page caching.
    variable_set('cache', TRUE);

    // Enable access logging.
    variable_set('statistics_enable_access_log', 1);
    variable_set('statistics_count_content_views', 1);

    // Clear the logs.
    db_truncate('accesslog');
    db_truncate('node_counter');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
