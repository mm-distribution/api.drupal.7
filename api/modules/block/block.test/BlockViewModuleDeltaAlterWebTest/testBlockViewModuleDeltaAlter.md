# BlockViewModuleDeltaAlterWebTest::testBlockViewModuleDeltaAlter()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 776–794 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L776-L794)
- **Class:** [BlockViewModuleDeltaAlterWebTest](../BlockViewModuleDeltaAlterWebTest.md)
- **Module/theme:** block

## Signature

```php
public function testBlockViewModuleDeltaAlter()
```

## Documentation

```text
Tests that the alter hook is called, even if the delta contains a hyphen.
```

## Code

```php
  public function testBlockViewModuleDeltaAlter() {
    $block = new stdClass;
    $block->module = 'block_test';
    $block->delta = 'test_underscore';
    $block->title = '';
    $render_array = _block_render_blocks(array('region' => $block));
    $render = array_pop($render_array);
    $test_underscore = $render->content['#markup'];
    $this->assertEqual($test_underscore, 'hook_block_view_MODULE_DELTA_alter', 'Found expected altered block content for delta with underscore');

    $block = new stdClass;
    $block->module = 'block_test';
    $block->delta = 'test-hyphen';
    $block->title = '';
    $render_array = _block_render_blocks(array('region' => $block));
    $render = array_pop($render_array);
    $test_hyphen = $render->content['#markup'];
    $this->assertEqual($test_hyphen, 'hook_block_view_MODULE_DELTA_alter', 'Hyphens (-) in block delta were replaced by underscore (_)');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
