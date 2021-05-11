def plugin_prefs(parent, cmdr, is_beta):

    PADX = 10
    BUTTONX = 12	# indent Checkbuttons and Radiobuttons
    PADY = 2		# close spacing

    output = config.getint('output') or (config.OUT_MKT_EDDN | config.OUT_SYS_EDDN)	# default settings

    eddnframe = nb.Frame(parent)

    HyperlinkLabel(eddnframe, text='Elite Dangerous Data Network', background=nb.Label().cget('background'), url='https://github.com/EDSM-NET/EDDN/wiki', underline=True).grid(padx=PADX, sticky=tk.W)	# Don't translate
    this.eddn_station= tk.IntVar(value = (output & config.OUT_MKT_EDDN) and 1)
    this.eddn_station_button = nb.Checkbutton(eddnframe, text=_('Send station data to the Elite Dangerous Data Network'), variable=this.eddn_station, command=prefsvarchanged)	# Output setting
    this.eddn_station_button.grid(padx=BUTTONX, pady=(5,0), sticky=tk.W)
    this.eddn_system = tk.IntVar(value = (output & config.OUT_SYS_EDDN) and 1)
    this.eddn_system_button = nb.Checkbutton(eddnframe, text=_('Send system and scan data to the Elite Dangerous Data Network'), variable=this.eddn_system, command=prefsvarchanged)	# Output setting new in E:D 2.2
    this.eddn_system_button.grid(padx=BUTTONX, pady=(5,0), sticky=tk.W)
    this.eddn_delay= tk.IntVar(value = (output & config.OUT_SYS_DELAY) and 1)
    this.eddn_delay_button = nb.Checkbutton(eddnframe, text=_('Delay sending until docked'), variable=this.eddn_delay)	# Output setting under 'Send system and scan data to the Elite Dangerous Data Network' new in E:D 2.2
    this.eddn_delay_button.grid(padx=BUTTONX, sticky=tk.W)

    return eddnframe 