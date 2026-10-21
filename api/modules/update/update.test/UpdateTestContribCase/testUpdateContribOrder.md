# UpdateTestContribCase::testUpdateContribOrder()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 367–424 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L367-L424)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

## Signature

```php
function testUpdateContribOrder()
```

## Documentation

```text
Tests that contrib projects are ordered by project name.

If a project contains multiple modules, we want to make sure that the
available updates report is sorted by the parent project names, not by the
names of the modules included in each project. In this test case, we have
two contrib projects, "BBB Update test" and "CCC Update test". However, we
have a module called "aaa_update_test" that's part of the "CCC Update test"
project. We need to make sure that we see the "BBB" project before the
"CCC" project, even though "CCC" includes a module that's processed first
if you sort alphabetically by module name (which is the order we see things
inside system_rebuild_module_data() for example).
```

## Code

```php
  function testUpdateContribOrder() {
    // We want core to be version 7.0.
    $system_info = array(
      '#all' => array(
        'version' => '7.0',
      ),
      // All the rest should be visible as contrib modules at version 7.x-1.0.

      // aaa_update_test needs to be part of the "CCC Update test" project,
      // which would throw off the report if we weren't properly sorting by
      // the project names.
      'aaa_update_test' => array(
        'project' => 'ccc_update_test',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),

      // This should be its own project, and listed first on the report.
      'bbb_update_test' => array(
        'project' => 'bbb_update_test',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),

      // This will contain both aaa_update_test and ccc_update_test, and
      // should come after the bbb_update_test project.
      'ccc_update_test' => array(
        'project' => 'ccc_update_test',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
    );
    variable_set('update_test_system_info', $system_info);
    $this->refreshUpdateStatus(array('drupal' => '0', '#all' => '1_0'));
    $this->standardTests();
    // We're expecting the report to say all projects are up to date.
    $this->assertText(t('Up to date'));
    $this->assertNoText(t('Update available'));
    // We want to see all 3 module names listed, since they'll show up either
    // as project names or as modules under the "Includes" listing.
    $this->assertText(t('AAA Update test'));
    $this->assertText(t('BBB Update test'));
    $this->assertText(t('CCC Update test'));
    // We want aaa_update_test included in the ccc_update_test project, not as
    // its own project on the report.
    $this->assertNoRaw(l(t('AAA Update test'), 'http://example.com/project/aaa_update_test'), 'Link to aaa_update_test project does not appear.');
    // The other two should be listed as projects.
    $this->assertRaw(l(t('BBB Update test'), 'http://example.com/project/bbb_update_test'), 'Link to bbb_update_test project appears.');
    $this->assertRaw(l(t('CCC Update test'), 'http://example.com/project/ccc_update_test'), 'Link to bbb_update_test project appears.');

    // We want to make sure we see the BBB project before the CCC project.
    // Instead of just searching for 'BBB Update test' or something, we want
    // to use the full markup that starts the project entry itself, so that
    // we're really testing that the project listings are in the right order.
    $bbb_project_link = '<div class="project"><a href="http://example.com/project/bbb_update_test">BBB Update test</a>';
    $ccc_project_link = '<div class="project"><a href="http://example.com/project/ccc_update_test">CCC Update test</a>';
    $this->assertTrue(strpos($this->drupalGetContent(), $bbb_project_link) < strpos($this->drupalGetContent(), $ccc_project_link), "'BBB Update test' project is listed before the 'CCC Update test' project");
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
