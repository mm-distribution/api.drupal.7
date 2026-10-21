# DashboardBlocksTestCase::testBlockAvailability()

- **Type:** Method
- **File:** [`modules/dashboard/dashboard.test`](../_file.md), lines 120–140 · [local source](../../../../../source/modules/dashboard/dashboard.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test#L120-L140)
- **Class:** [DashboardBlocksTestCase](../DashboardBlocksTestCase.md)
- **Module/theme:** dashboard

## Signature

```php
function testBlockAvailability()
```

## Documentation

```text
Tests that administrative blocks are available for the dashboard.
```

## Code

```php
  function testBlockAvailability() {
    // Test "Recent comments", which should be available (defined as
    // "administrative") but not enabled.
    $this->drupalGet('admin/dashboard');
    $this->assertNoText(t('Recent comments'), '"Recent comments" not on dashboard.');
    $this->drupalGet('admin/dashboard/drawer');
    $this->assertText(t('Recent comments'), 'Drawer of disabled blocks includes a block defined as "administrative".');
    $this->assertNoText(t('Syndicate'), 'Drawer of disabled blocks excludes a block not defined as "administrative".');
    $this->drupalGet('admin/dashboard/configure');
    $elements = $this->xpath('//select[@id=:id]//option[@selected="selected"]', array(':id' => 'edit-blocks-comment-recent-region'));
    $this->assertTrue($elements[0]['value'] == 'dashboard_inactive', 'A block defined as "administrative" defaults to dashboard_inactive.');

    // Now enable the block on the dashboard.
    $values = array();
    $values['blocks[comment_recent][region]'] = 'dashboard_main';
    $this->drupalPost('admin/dashboard/configure', $values, t('Save blocks'));
    $this->drupalGet('admin/dashboard');
    $this->assertText(t('Recent comments'), '"Recent comments" was placed on dashboard.');
    $this->drupalGet('admin/dashboard/drawer');
    $this->assertNoText(t('Recent comments'), 'Drawer of disabled blocks excludes enabled blocks.');
  }
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.test](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test) · Licensed GPL-2.0-or-later (see LICENSE)._
