# block_admin_display_form()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 78–165 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L78-L165)
- **Module/theme:** block
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function block_admin_display_form($form, &$form_state, $blocks, $theme, $block_regions = NULL)
```

## Documentation

```text
Form constructor for the main block administration form.

@param $blocks
  An array of blocks, as returned by block_admin_display_prepare_blocks().
@param $theme
  A string representing the name of the theme to edit blocks for.
@param $block_regions
  (optional) An array of regions in which the blocks will be allowed to be
  placed. Defaults to all visible regions for the theme whose blocks are
  being configured. In all cases, a dummy region for disabled blocks will
  also be displayed.

@return
  An array representing the form definition.

@ingroup forms
@see block_admin_display_form_submit()
```

## Code

```php
function block_admin_display_form($form, &$form_state, $blocks, $theme, $block_regions = NULL) {

  $form['#attached']['css'] = array(drupal_get_path('module', 'block') . '/block.css');

  // Get a list of block regions if one was not provided.
  if (!isset($block_regions)) {
    $block_regions = system_region_list($theme, REGIONS_VISIBLE);
  }

  // Weights range from -delta to +delta, so delta should be at least half
  // of the amount of blocks present. This makes sure all blocks in the same
  // region get an unique weight.
  $weight_delta = round(count($blocks) / 2);

  // Build the form tree.
  $form['edited_theme'] = array(
    '#type' => 'value',
    '#value' => $theme,
  );
  $form['block_regions'] = array(
    '#type' => 'value',
    // Add a last region for disabled blocks.
    '#value' => $block_regions + array(BLOCK_REGION_NONE => BLOCK_REGION_NONE),
  );
  $form['blocks'] = array();
  $form['#tree'] = TRUE;

  foreach ($blocks as $i => $block) {
    $key = $block['module'] . '_' . $block['delta'];
    $form['blocks'][$key]['module'] = array(
      '#type' => 'value',
      '#value' => $block['module'],
    );
    $form['blocks'][$key]['delta'] = array(
      '#type' => 'value',
      '#value' => $block['delta'],
    );
    $form['blocks'][$key]['info'] = array(
      '#markup' => check_plain($block['info']),
    );
    $form['blocks'][$key]['theme'] = array(
      '#type' => 'hidden',
      '#value' => $theme,
    );
    $form['blocks'][$key]['weight'] = array(
      '#type' => 'weight',
      '#default_value' => $block['weight'],
      '#delta' => $weight_delta,
      '#title_display' => 'invisible',
      '#title' => t('Weight for @block block', array('@block' => $block['info'])),
    );
    $form['blocks'][$key]['region'] = array(
      '#type' => 'select',
      '#default_value' => $block['region'] != BLOCK_REGION_NONE ? $block['region'] : NULL,
      '#empty_value' => BLOCK_REGION_NONE,
      '#title_display' => 'invisible',
      '#title' => t('Region for @block block', array('@block' => $block['info'])),
      '#options' => $block_regions,
    );
    $form['blocks'][$key]['configure'] = array(
      '#type' => 'link',
      '#title' => t('configure'),
      '#href' => 'admin/structure/block/manage/' . $block['module'] . '/' . $block['delta'] . '/configure',
    );
    if ($block['module'] == 'block') {
      $form['blocks'][$key]['delete'] = array(
        '#type' => 'link',
        '#title' => t('delete'),
        '#href' => 'admin/structure/block/manage/' . $block['module'] . '/' . $block['delta'] . '/delete',
     );
    }
  }
  // Do not allow disabling the main system content block when it is present.
  if (isset($form['blocks']['system_main']['region'])) {
    $form['blocks']['system_main']['region']['#required'] = TRUE;
  }

  $form['actions'] = array(
    '#tree' => FALSE,
    '#type' => 'actions',
  );
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save blocks'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
