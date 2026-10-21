# StatisticsAdminTestCase::setUp()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 337–342 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L337-L342)
- **Class:** [StatisticsAdminTestCase](../StatisticsAdminTestCase.md)
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
    $this->privileged_user = $this->drupalCreateUser(array('access statistics', 'administer statistics', 'view post access counter', 'create page content'));
    $this->drupalLogin($this->privileged_user);
    $this->test_node = $this->drupalCreateNode(array('type' => 'page', 'uid' => $this->privileged_user->uid));
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
