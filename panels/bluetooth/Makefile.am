# This is used in PANEL_CFLAGS
cappletname = bluetooth

ccpanelsdir = $(PANELS_DIR)
ccpanels_LTLIBRARIES = libbluetooth.la

AM_CPPFLAGS = 						\
	$(PANEL_CFLAGS)					\
	$(BLUETOOTH_CFLAGS)				\
	-LOCALEDIR="\"$(datadir)/locale\""	\
	-DPKGDATADIR="\"$(pkgdatadir)\""
	$(NULL)

BUILT_SOURCES =				\
	cc-bluetooth-resources.h	\
	cc-bluetooth-resources.c

libbluetooth_la_SOURCES =			\
	$(BUILT_SOURCES)			\
	cc-bluetooth-panel.c			\
	cc-bluetooth-panel.h

libbluetooth_la_LIBADD = $(PANEL_LIBS) $(BLUETOOTH_LIBS)
libbluetooth_la_LDFLAGS = $(PANEL_LDFLAGS)

resource_files = $(shell glib-compile-resources --sourcedir=$(srcdir) --generate-dependencies $(srcdir)/bluetooth.gresource.xml)
cc-bluetooth-resources.c: bluetooth.gresource.xml $(resource_files)
	$(AM_V_GEN) glib-compile-resources --target=$@ --sourcedir=$(srcdir) --generate-source --c-name cc_bluetooth $<
cc-bluetooth-resources.h: bluetooth.gresource.xml $(resource_files)
	$(AM_V_GEN) glib-compile-resources --target=$@ --sourcedir=$(srcdir) --generate-header --c-name cc_bluetooth $<

desktopdir = $(datadir)/applications
desktop_in_in_files = cinnamon-bluetooth-properties.desktop.in.in
desktop_in_files = cinnamon-bluetooth-properties.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)
@INTLTOOL_DESKTOP_RULE@

CLEANFILES = $(desktop_DATA) $(BUILT_SOURCES)
EXTRA_DIST = $(man_MANS) $(desktop_in_in_files) $(resource_files) bluetooth.gresource.xml

-include $(top_srcdir)/git.mk
