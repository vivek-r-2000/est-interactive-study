# Simulators for Lectures 13, 14, 15

SIMULATORS_4 = {
    "sim_13": """
    <div class="eco-card p-6 border-emerald-800 bg-[#06150e]">
      <div class="flex flex-wrap items-center justify-between gap-2 mb-4 pb-3 border-b border-emerald-900/80">
        <div>
          <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Simulator 13</span>
          <h3 class="text-xl font-black text-white mt-1">Hydroelectric Dam Submergence vs Ecological Valuation</h3>
        </div>
        <span class="text-xs text-emerald-400 font-mono">Silent Valley & Narmada Tradeoff Model</span>
      </div>
      <p class="text-xs text-slate-300 mb-6">
        Simulate the techno-ecological conflict of large river valley projects. Adjust dam reservoir height to observe installed hydroelectric capacity, forest submergence area, displaced population, and the environmental resistance index.
      </p>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Controls -->
        <div class="lg:col-span-5 space-y-4 bg-[#081a12] p-4 rounded-xl border border-emerald-900/60">
          <div>
            <div class="flex justify-between text-xs font-semibold mb-1">
              <span class="text-slate-300">Dam Wall Height ($H$):</span>
              <span id="dam_h_val" class="text-emerald-400 font-mono font-bold">85 m</span>
            </div>
            <input type="range" id="dam_h_slider" min="30" max="140" step="5" value="85" class="w-full accent-emerald-500" oninput="updateDamSim()">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-1">
              <span>30 m (Low Run-of-River)</span>
              <span>140 m (Mega Dam)</span>
            </div>
          </div>

          <div>
            <div class="flex justify-between text-xs font-semibold mb-1">
              <span class="text-slate-300">Ecosystem Sensitivity Factor:</span>
              <span id="dam_sens_val" class="text-teal-400 font-mono font-bold">High (Silent Valley Rainforest)</span>
            </div>
            <select id="dam_sens_select" class="w-full bg-[#05120c] border border-emerald-800 text-xs text-emerald-200 rounded-lg p-2 font-mono" onchange="updateDamSim()">
              <option value="1.0">Low (Degraded Scrubland / Sparse)</option>
              <option value="2.5">Moderate (Deciduous River Valley)</option>
              <option value="5.0" selected>High (Endemic Pristine Evergreen Forest)</option>
            </select>
          </div>

          <div class="p-3 bg-[#05120c] rounded-lg border border-emerald-900 text-xs text-slate-300 space-y-1 font-mono">
            <div>• Hydropower Power Formula: $P = \\eta \\cdot \\rho \\cdot g \\cdot Q \\cdot H$</div>
            <div>• Submergence scaling: $\\text{Area} \\propto H^{1.85}$</div>
          </div>
        </div>

        <!-- Live Outputs -->
        <div class="lg:col-span-7 grid grid-cols-2 gap-3">
          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Installed Power</span>
            <div id="dam_power_out" class="text-2xl font-black text-emerald-400 font-mono my-2">120 MW</div>
            <span class="text-[10px] text-slate-400">Clean electrical grid output</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Forest Submerged</span>
            <div id="dam_area_out" class="text-2xl font-black text-amber-400 font-mono my-2">8.3 sq km</div>
            <span class="text-[10px] text-slate-400">Canopy lost beneath water</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Displaced People</span>
            <div id="dam_disp_out" class="text-2xl font-black text-red-400 font-mono my-2">3,400</div>
            <span class="text-[10px] text-slate-400">Rural / tribal villagers</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Protest & Agitation Index</span>
            <div id="dam_protest_out" class="text-2xl font-black text-purple-400 font-mono my-2">Severe (85/100)</div>
            <span class="text-[10px] text-slate-400">Civil society resistance likelihood</span>
          </div>
        </div>
      </div>
    </div>
    <script>
      function updateDamSim() {
        const h = parseFloat(document.getElementById('dam_h_slider').value);
        const sens = parseFloat(document.getElementById('dam_sens_select').value);
        document.getElementById('dam_h_val').innerText = h + ' m';
        
        // Power calculation (approx 1.4 MW per meter of head for 100 m3/s flow)
        const mw = Math.round(1.41 * h);
        // Submergence area scales non-linearly
        const sqkm = (0.0018 * Math.pow(h, 1.88)).toFixed(1);
        // Displacement
        const disp = Math.round(12 * Math.pow(h, 1.35));
        // Protest index
        const protestScore = Math.min(100, Math.round((sqkm * sens * 2.2) + (disp / 80)));
        let protestText = 'Low (30/100)';
        if (protestScore > 75) protestText = 'Extreme (' + protestScore + '/100)';
        else if (protestScore > 50) protestText = 'High (' + protestScore + '/100)';
        else if (protestScore > 25) protestText = 'Moderate (' + protestScore + '/100)';

        document.getElementById('dam_power_out').innerText = mw + ' MW';
        document.getElementById('dam_area_out').innerText = sqkm + ' sq km';
        document.getElementById('dam_disp_out').innerText = disp.toLocaleString();
        document.getElementById('dam_protest_out').innerText = protestText;
      }
    </script>
    """,

    "sim_14": """
    <div class="eco-card p-6 border-emerald-800 bg-[#06150e]">
      <div class="flex flex-wrap items-center justify-between gap-2 mb-4 pb-3 border-b border-emerald-900/80">
        <div>
          <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Simulator 14</span>
          <h3 class="text-xl font-black text-white mt-1">Green Datacenter PUE & Server Virtualization Calculator</h3>
        </div>
        <span class="text-xs text-emerald-400 font-mono">Sustainable IT Power Architecture</span>
      </div>
      <p class="text-xs text-slate-300 mb-6">
        Model energy efficiency and carbon emissions in datacenter infrastructure. Adjust physical server count, virtualization consolidation ratio, and cooling methodology to observe Power Usage Effectiveness (PUE), annual energy bills, and avoided $CO_2e$.
      </p>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Controls -->
        <div class="lg:col-span-5 space-y-4 bg-[#081a12] p-4 rounded-xl border border-emerald-900/60">
          <div>
            <div class="flex justify-between text-xs font-semibold mb-1">
              <span class="text-slate-300">Legacy Physical Servers:</span>
              <span id="pue_servers_val" class="text-emerald-400 font-mono font-bold">1,000</span>
            </div>
            <input type="range" id="pue_servers_slider" min="100" max="5000" step="100" value="1000" class="w-full accent-emerald-500" oninput="updatePueSim()">
          </div>

          <div>
            <div class="flex justify-between text-xs font-semibold mb-1">
              <span class="text-slate-300">Virtualization Consolidation:</span>
              <span id="pue_virt_val" class="text-teal-400 font-mono font-bold">8:1 (8 VM per physical server)</span>
            </div>
            <input type="range" id="pue_virt_slider" min="1" max="20" step="1" value="8" class="w-full accent-teal-500" oninput="updatePueSim()">
          </div>

          <div>
            <div class="flex justify-between text-xs font-semibold mb-1">
              <span class="text-slate-300">Cooling Technology:</span>
              <span id="pue_cooling_val" class="text-cyan-400 font-mono font-bold">Free-Air / Evaporative (PUE 1.25)</span>
            </div>
            <select id="pue_cooling_select" class="w-full bg-[#05120c] border border-emerald-800 text-xs text-emerald-200 rounded-lg p-2 font-mono" onchange="updatePueSim()">
              <option value="2.0">Standard DX Air Conditioning (Legacy PUE 2.0)</option>
              <option value="1.5">Chilled Water Plant with Economizer (PUE 1.5)</option>
              <option value="1.25" selected>Free-Air Evaporative Cooling (PUE 1.25)</option>
              <option value="1.08">Direct Liquid Immersion Cooling (Cutting-Edge PUE 1.08)</option>
            </select>
          </div>
        </div>

        <!-- Live Outputs -->
        <div class="lg:col-span-7 grid grid-cols-2 gap-3">
          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Consolidated Servers</span>
            <div id="pue_active_out" class="text-2xl font-black text-emerald-400 font-mono my-2">125 Units</div>
            <span class="text-[10px] text-emerald-300">875 idle machines retired</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Achieved Facility PUE</span>
            <div id="pue_val_out" class="text-2xl font-black text-cyan-400 font-mono my-2">1.25</div>
            <span class="text-[10px] text-slate-400">Total Power / IT Power</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Annual Electricity Saved</span>
            <div id="pue_kwh_out" class="text-2xl font-black text-amber-400 font-mono my-2">3.83 GWh/yr</div>
            <span class="text-[10px] text-slate-400">~ $383,000 cost savings</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Avoided Emissions</span>
            <div id="pue_co2_out" class="text-2xl font-black text-teal-300 font-mono my-2">2,757 tCO₂e/yr</div>
            <span class="text-[10px] text-slate-400">Based on 0.72 kg CO₂/kWh grid</span>
          </div>
        </div>
      </div>
    </div>
    <script>
      function updatePueSim() {
        const rawServers = parseInt(document.getElementById('pue_servers_slider').value);
        const ratio = parseInt(document.getElementById('pue_virt_slider').value);
        const pue = parseFloat(document.getElementById('pue_cooling_select').value);

        document.getElementById('pue_servers_val').innerText = rawServers.toLocaleString();
        document.getElementById('pue_virt_val').innerText = ratio + ':1 (' + ratio + ' VM per server)';

        const activeServers = Math.ceil(rawServers / ratio);
        // Server average draw: 400W active
        const legacyKwh = (rawServers * 0.400 * 8760 * 2.0); // Baseline legacy PUE 2.0
        const modernKwh = (activeServers * 0.450 * 8760 * pue);
        const savedKwh = Math.max(0, legacyKwh - modernKwh);
        const savedGwh = (savedKwh / 1000000).toFixed(2);
        const co2Saved = Math.round(savedKwh * 0.00072);

        document.getElementById('pue_active_out').innerText = activeServers.toLocaleString() + ' Units';
        document.getElementById('pue_val_out').innerText = pue.toFixed(2);
        document.getElementById('pue_kwh_out').innerText = savedGwh + ' GWh/yr';
        document.getElementById('pue_co2_out').innerText = co2Saved.toLocaleString() + ' tCO₂e/yr';
      }
    </script>
    """,

    "sim_15": """
    <div class="eco-card p-6 border-emerald-800 bg-[#06150e]">
      <div class="flex flex-wrap items-center justify-between gap-2 mb-4 pb-3 border-b border-emerald-900/80">
        <div>
          <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Simulator 15</span>
          <h3 class="text-xl font-black text-white mt-1">Industrial Symbiosis & Circular Material Exchange Model</h3>
        </div>
        <span class="text-xs text-emerald-400 font-mono">Kalundborg Closed-Loop Network</span>
      </div>
      <p class="text-xs text-slate-300 mb-6">
        Model circular material flows in an eco-industrial park. Toggle industrial byproduct links to turn waste streams (flue gas SO₂, waste steam, refinery cooling water, organic fermentation slurry) into valuable commercial feedstocks.
      </p>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Toggles -->
        <div class="lg:col-span-5 space-y-3 bg-[#081a12] p-4 rounded-xl border border-emerald-900/60 text-xs">
          <label class="flex items-center gap-3 p-2.5 bg-[#05120c] rounded-lg border border-emerald-900 cursor-pointer hover:border-emerald-600 transition-all">
            <input type="checkbox" id="sym_link1" class="accent-emerald-500 w-4 h-4" checked onchange="updateSymSim()">
            <div>
              <strong class="text-emerald-300 block">Flue-Gas Desulfurization $\to$ Synthetic Gypsum</strong>
              <span class="text-[11px] text-slate-400">Power station SO₂ scrubber supplies Gyproc wallboard factory</span>
            </div>
          </label>

          <label class="flex items-center gap-3 p-2.5 bg-[#05120c] rounded-lg border border-emerald-900 cursor-pointer hover:border-emerald-600 transition-all">
            <input type="checkbox" id="sym_link2" class="accent-emerald-500 w-4 h-4" checked onchange="updateSymSim()">
            <div>
              <strong class="text-emerald-300 block">Power Station Excess Steam $\to$ Refinery & Pharma</strong>
              <span class="text-[11px] text-slate-400">Replaces standalone gas boilers; recovers 80% waste heat</span>
            </div>
          </label>

          <label class="flex items-center gap-3 p-2.5 bg-[#05120c] rounded-lg border border-emerald-900 cursor-pointer hover:border-emerald-600 transition-all">
            <input type="checkbox" id="sym_link3" class="accent-emerald-500 w-4 h-4" checked onchange="updateSymSim()">
            <div>
              <strong class="text-emerald-300 block">Fermentation Biomass Sludge $\to$ Agricultural Fertilizer</strong>
              <span class="text-[11px] text-slate-400">Novo Nordisk yeast biomass fertilizes 3,000 local hectares</span>
            </div>
          </label>

          <label class="flex items-center gap-3 p-2.5 bg-[#05120c] rounded-lg border border-emerald-900 cursor-pointer hover:border-emerald-600 transition-all">
            <input type="checkbox" id="sym_link4" class="accent-emerald-500 w-4 h-4" checked onchange="updateSymSim()">
            <div>
              <strong class="text-emerald-300 block">Warm Cooling Water $\to$ Commercial Fish Aquaculture</strong>
              <span class="text-[11px] text-slate-400">Power plant thermal effluent warms 57 aquaculture trout ponds</span>
            </div>
          </label>
        </div>

        <!-- Live Metrics -->
        <div class="lg:col-span-7 grid grid-cols-2 gap-3">
          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Landfill Waste Diverted</span>
            <div id="sym_landfill_out" class="text-2xl font-black text-emerald-400 font-mono my-2">92%</div>
            <span class="text-[10px] text-slate-400">Solid byproducts monetized</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Virgin Gypsum Saved</span>
            <div id="sym_gypsum_out" class="text-2xl font-black text-cyan-400 font-mono my-2">200,000 t/yr</div>
            <span class="text-[10px] text-slate-400">Open-cast mining avoided</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Water Recycled</span>
            <div id="sym_water_out" class="text-2xl font-black text-amber-400 font-mono my-2">1.2 Million m³</div>
            <span class="text-[10px] text-slate-400">Freshwater withdrawal reduced</span>
          </div>

          <div class="p-4 bg-[#081a12] border border-emerald-900/80 rounded-xl flex flex-col justify-between">
            <span class="text-[11px] font-bold text-slate-400 uppercase font-mono">Overall Symbiosis Index</span>
            <div id="sym_index_out" class="text-2xl font-black text-teal-300 font-mono my-2">World-Class (94/100)</div>
            <span class="text-[10px] text-slate-400">Circular eco-industrial rating</span>
          </div>
        </div>
      </div>
    </div>
    <script>
      function updateSymSim() {
        const l1 = document.getElementById('sym_link1').checked;
        const l2 = document.getElementById('sym_link2').checked;
        const l3 = document.getElementById('sym_link3').checked;
        const l4 = document.getElementById('sym_link4').checked;

        let diverted = 0;
        let gypsum = 0;
        let water = 0;
        let score = 0;

        if (l1) { diverted += 35; gypsum += 200000; score += 25; }
        if (l2) { diverted += 25; water += 0.5; score += 25; }
        if (l3) { diverted += 22; score += 24; }
        if (l4) { diverted += 10; water += 0.7; score += 20; }

        let rating = 'Linear / Low (' + score + '/100)';
        if (score >= 90) rating = 'World-Class (' + score + '/100)';
        else if (score >= 60) rating = 'High Symbiosis (' + score + '/100)';
        else if (score >= 30) rating = 'Developing (' + score + '/100)';

        document.getElementById('sym_landfill_out').innerText = Math.min(100, diverted) + '%';
        document.getElementById('sym_gypsum_out').innerText = gypsum.toLocaleString() + ' t/yr';
        document.getElementById('sym_water_out').innerText = water.toFixed(1) + ' Million m³';
        document.getElementById('sym_index_out').innerText = rating;
      }
    </script>
    """
}
