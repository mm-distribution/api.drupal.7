# system_library()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1103–1677 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1103-L1677)
- **Module/theme:** system
- **Implements:** [hook_library()](../system.api.php/hook_library.md)

## Signature

```php
function system_library()
```

## Documentation

```text
Implements hook_library().
```

## Code

```php
function system_library() {
  // Drupal's Ajax framework.
  $libraries['drupal.ajax'] = array(
    'title' => 'Drupal AJAX',
    'website' => 'http://api.drupal.org/api/drupal/includes--ajax.inc/group/ajax/7',
    'version' => VERSION,
    'js' => array(
      'misc/ajax.js' => array('group' => JS_LIBRARY, 'weight' => 2),
    ),
    'dependencies' => array(
      array('system', 'drupal.progress'),
    ),
  );

  // Drupal's batch API.
  $libraries['drupal.batch'] = array(
    'title' => 'Drupal batch API',
    'version' => VERSION,
    'js' => array(
      'misc/batch.js' => array('group' => JS_DEFAULT, 'cache' => FALSE),
    ),
    'dependencies' => array(
      array('system', 'drupal.progress'),
    ),
  );

  // Drupal's progress indicator.
  $libraries['drupal.progress'] = array(
    'title' => 'Drupal progress indicator',
    'version' => VERSION,
    'js' => array(
      'misc/progress.js' => array('group' => JS_DEFAULT),
    ),
  );

  // Drupal's form library.
  $libraries['drupal.form'] = array(
    'title' => 'Drupal form library',
    'version' => VERSION,
    'js' => array(
      'misc/form.js' => array('group' => JS_LIBRARY, 'weight' => 1),
    ),
  );

  // Drupal's form single submit library.
  $libraries['drupal.form-single-submit'] = array(
    'title' => 'Drupal form single submit library',
    'version' => VERSION,
    'js' => array(
      'misc/form-single-submit.js' => array('group' => JS_LIBRARY, 'weight' => 1),
    ),
  );

  // Drupal's states library.
  $libraries['drupal.states'] = array(
    'title' => 'Drupal states',
    'version' => VERSION,
    'js' => array(
      'misc/states.js' => array('group' => JS_LIBRARY, 'weight' => 1),
    ),
  );

  // Drupal's collapsible fieldset.
  $libraries['drupal.collapse'] = array(
    'title' => 'Drupal collapsible fieldset',
    'version' => VERSION,
    'js' => array(
      'misc/collapse.js' => array('group' => JS_DEFAULT),
    ),
    'dependencies' => array(
      // collapse.js relies on drupalGetSummary in form.js
      array('system', 'drupal.form'),
    ),
  );

  // Drupal's resizable textarea.
  $libraries['drupal.textarea'] = array(
    'title' => 'Drupal resizable textarea',
    'version' => VERSION,
    'js' => array(
      'misc/textarea.js' => array('group' => JS_DEFAULT),
    ),
  );

  // Drupal's autocomplete widget.
  $libraries['drupal.autocomplete'] = array(
    'title' => 'Drupal autocomplete',
    'version' => VERSION,
    'js' => array(
      'misc/autocomplete.js' => array('group' => JS_DEFAULT),
    ),
  );

  // jQuery.
  $libraries['jquery'] = array(
    'title' => 'jQuery',
    'website' => 'http://jquery.com',
    'version' => '1.4.4',
    'js' => array(
      'misc/jquery.js' => array('group' => JS_LIBRARY, 'weight' => -20),
      // These include security fixes, so assign a weight that makes them load
      // as soon after jquery.js is loaded as possible.
      'misc/jquery-extend-3.4.0.js' => array('group' => JS_LIBRARY, 'weight' => -19),
      'misc/jquery-html-prefilter-3.5.0-backport.js' => array('group' => JS_LIBRARY, 'weight' => -19),
    ),
  );

  // jQuery Once.
  $libraries['jquery.once'] = array(
    'title' => 'jQuery Once',
    'website' => 'http://plugins.jquery.com/project/once',
    'version' => '1.2',
    'js' => array(
      'misc/jquery.once.js' => array('group' => JS_LIBRARY, 'weight' => -19),
    ),
  );

  // jQuery Form Plugin.
  $libraries['jquery.form'] = array(
    'title' => 'jQuery Form Plugin',
    'website' => 'http://malsup.com/jquery/form/',
    'version' => '2.52',
    'js' => array(
      'misc/jquery.form.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'jquery.cookie'),
    ),
  );

  // jQuery BBQ plugin.
  $libraries['jquery.bbq'] = array(
    'title' => 'jQuery BBQ',
    'website' => 'http://benalman.com/projects/jquery-bbq-plugin/',
    'version' => '1.2.1',
    'js' => array(
      'misc/jquery.ba-bbq.js' => array(),
    ),
  );

  // Vertical Tabs.
  $libraries['drupal.vertical-tabs'] = array(
    'title' => 'Vertical Tabs',
    'website' => 'http://drupal.org/node/323112',
    'version' => '1.0',
    'js' => array(
      'misc/vertical-tabs.js' => array(),
    ),
    'css' => array(
      'misc/vertical-tabs.css' => array(),
    ),
    'dependencies' => array(
      // Vertical tabs relies on drupalGetSummary in form.js
      array('system', 'drupal.form'),
    ),
  );

  // Farbtastic.
  $libraries['farbtastic'] = array(
    'title' => 'Farbtastic',
    'website' => 'http://code.google.com/p/farbtastic/',
    'version' => '1.2',
    'js' => array(
      'misc/farbtastic/farbtastic.js' => array(),
    ),
    'css' => array(
      'misc/farbtastic/farbtastic.css' => array(),
    ),
  );

  // Cookie.
  $libraries['jquery.cookie'] = array(
    'title' => 'Cookie',
    'website' => 'http://plugins.jquery.com/project/cookie',
    'version' => '1.0',
    'js' => array(
      'misc/jquery.cookie.js' => array(),
    ),
  );

  // jQuery UI.
  $libraries['ui'] = array(
    'title' => 'jQuery UI: Core',
    'website' => 'http://jqueryui.com',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.core.min.js' => array('group' => JS_LIBRARY, 'weight' => -11),
    ),
    'css' => array(
      'misc/ui/jquery.ui.core.css' => array(),
      'misc/ui/jquery.ui.theme.css' => array(),
    ),
  );
  $libraries['ui.accordion'] = array(
    'title' => 'jQuery UI: Accordion',
    'website' => 'http://jqueryui.com/demos/accordion/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.accordion.min.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.accordion.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
    ),
  );
  $libraries['ui.autocomplete'] = array(
    'title' => 'jQuery UI: Autocomplete',
    'website' => 'http://jqueryui.com/demos/autocomplete/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.autocomplete.min.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.autocomplete.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
      array('system', 'ui.position'),
    ),
  );
  $libraries['ui.button'] = array(
    'title' => 'jQuery UI: Button',
    'website' => 'http://jqueryui.com/demos/button/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.button.min.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.button.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
    ),
  );
  $libraries['ui.datepicker'] = array(
    'title' => 'jQuery UI: Date Picker',
    'website' => 'http://jqueryui.com/demos/datepicker/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.datepicker.min.js' => array(),
      'misc/ui/jquery.ui.datepicker-1.13.0-backport.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.datepicker.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui'),
    ),
  );
  $libraries['ui.dialog'] = array(
    'title' => 'jQuery UI: Dialog',
    'website' => 'http://jqueryui.com/demos/dialog/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.dialog.min.js' =>  array(),
      'misc/ui/jquery.ui.dialog-1.13.0-backport.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.dialog.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
      array('system', 'ui.button'),
      array('system', 'ui.draggable'),
      array('system', 'ui.mouse'),
      array('system', 'ui.position'),
      array('system', 'ui.resizable'),
    ),
  );
  $libraries['ui.draggable'] = array(
    'title' => 'jQuery UI: Draggable',
    'website' => 'http://jqueryui.com/demos/draggable/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.draggable.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
      array('system', 'ui.mouse'),
    ),
  );
  $libraries['ui.droppable'] = array(
    'title' => 'jQuery UI: Droppable',
    'website' => 'http://jqueryui.com/demos/droppable/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.droppable.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
      array('system', 'ui.mouse'),
      array('system', 'ui.draggable'),
    ),
  );
  $libraries['ui.mouse'] = array(
    'title' => 'jQuery UI: Mouse',
    'website' => 'http://docs.jquery.com/UI/Mouse',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.mouse.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
    ),
  );
  $libraries['ui.position'] = array(
    'title' => 'jQuery UI: Position',
    'website' => 'http://jqueryui.com/demos/position/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.position.min.js' => array(),
      'misc/ui/jquery.ui.position-1.13.0-backport.js' => array(),
    ),
  );
  $libraries['ui.progressbar'] = array(
    'title' => 'jQuery UI: Progress Bar',
    'website' => 'http://jqueryui.com/demos/progressbar/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.progressbar.min.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.progressbar.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
    ),
  );
  $libraries['ui.resizable'] = array(
    'title' => 'jQuery UI: Resizable',
    'website' => 'http://jqueryui.com/demos/resizable/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.resizable.min.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.resizable.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
      array('system', 'ui.mouse'),
    ),
  );
  $libraries['ui.selectable'] = array(
    'title' => 'jQuery UI: Selectable',
    'website' => 'http://jqueryui.com/demos/selectable/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.selectable.min.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.selectable.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
      array('system', 'ui.mouse'),
    ),
  );
  $libraries['ui.slider'] = array(
    'title' => 'jQuery UI: Slider',
    'website' => 'http://jqueryui.com/demos/slider/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.slider.min.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.slider.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
      array('system', 'ui.mouse'),
    ),
  );
  $libraries['ui.sortable'] = array(
    'title' => 'jQuery UI: Sortable',
    'website' => 'http://jqueryui.com/demos/sortable/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.sortable.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
      array('system', 'ui.mouse'),
    ),
  );
  $libraries['ui.tabs'] = array(
    'title' => 'jQuery UI: Tabs',
    'website' => 'http://jqueryui.com/demos/tabs/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.tabs.min.js' => array(),
    ),
    'css' => array(
      'misc/ui/jquery.ui.tabs.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui.widget'),
    ),
  );
  $libraries['ui.widget'] = array(
    'title' => 'jQuery UI: Widget',
    'website' => 'http://docs.jquery.com/UI/Widget',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.ui.widget.min.js' => array('group' => JS_LIBRARY, 'weight' => -10),
    ),
    'dependencies' => array(
      array('system', 'ui'),
    ),
  );
  $libraries['effects'] = array(
    'title' => 'jQuery UI: Effects',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.core.min.js' => array('group' => JS_LIBRARY, 'weight' => -9),
    ),
  );
  $libraries['effects.blind'] = array(
    'title' => 'jQuery UI: Effects Blind',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.blind.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.bounce'] = array(
    'title' => 'jQuery UI: Effects Bounce',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.bounce.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.clip'] = array(
    'title' => 'jQuery UI: Effects Clip',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.clip.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.drop'] = array(
    'title' => 'jQuery UI: Effects Drop',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.drop.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.explode'] = array(
    'title' => 'jQuery UI: Effects Explode',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.explode.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.fade'] = array(
    'title' => 'jQuery UI: Effects Fade',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.fade.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.fold'] = array(
    'title' => 'jQuery UI: Effects Fold',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.fold.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.highlight'] = array(
    'title' => 'jQuery UI: Effects Highlight',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.highlight.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.pulsate'] = array(
    'title' => 'jQuery UI: Effects Pulsate',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.pulsate.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.scale'] = array(
    'title' => 'jQuery UI: Effects Scale',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.scale.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.shake'] = array(
    'title' => 'jQuery UI: Effects Shake',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.shake.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.slide'] = array(
    'title' => 'jQuery UI: Effects Slide',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.slide.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );
  $libraries['effects.transfer'] = array(
    'title' => 'jQuery UI: Effects Transfer',
    'website' => 'http://jqueryui.com/demos/effect/',
    'version' => '1.8.7',
    'js' => array(
      'misc/ui/jquery.effects.transfer.min.js' => array(),
    ),
    'dependencies' => array(
      array('system', 'effects'),
    ),
  );

  // These library names are deprecated. Earlier versions of Drupal 7 didn't
  // consistently namespace their libraries, so these names are included for
  // backwards compatibility with those versions.
  $libraries['once'] = &$libraries['jquery.once'];
  $libraries['form'] = &$libraries['jquery.form'];
  $libraries['jquery-bbq'] = &$libraries['jquery.bbq'];
  $libraries['vertical-tabs'] = &$libraries['drupal.vertical-tabs'];
  $libraries['cookie'] = &$libraries['jquery.cookie'];

  return $libraries;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
